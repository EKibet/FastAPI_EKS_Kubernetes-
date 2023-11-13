from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from ecommerce import db
from . import schema
from . import services, validator

router = APIRouter(tags=["users"], prefix="/user")


@router.post('/registration', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    user = await validator.verify_email_exist(request.email, database)
    if user:
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists in the system"
        )

    new_user = await services.new_user_register(request, database)
    return new_user


@router.get('/get_users', response_model=List[schema.DisplayUser])
async def get_users(database: Session = Depends(db.get_db)):
    users = await services.get_all_users(database)

    return users


@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    user = await services.get_single_user(user_id, database)
    return user


@router.delete('/delete_user/{user_id}', response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id, database: Session = Depends(db.get_db)):
    await services.delete_user(user_id, database)

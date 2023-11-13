from typing import List, Optional

from fastapi import HTTPException, status

from . import schema
from .models import User


async def new_user_register(request: schema.User, database) -> User:
    new_user = User(name=request.name, email=request.email)
    new_user.set_password(request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)

    return new_user


async def get_all_users(database) -> List[User]:
    all_users = database.query(User).all()
    return all_users


async def get_single_user(user_id: int, database) -> Optional[User]:
    get_user = database.query(User).get(user_id)
    if not get_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    return get_user


async def delete_user(user_id, database):
    get_user = database.query(User).get(user_id)
    if not get_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    database.query(User).filter(User.id==user_id).delete()
    database.commit()

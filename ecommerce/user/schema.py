from pydantic import BaseModel, constr, EmailStr


class User(BaseModel):
    email: EmailStr
    name: constr(min_length=2, max_length=50)
    password: str


class DisplayUser(BaseModel):
    id: int
    name: str
    email: str

    class Config:  # controls the behaviour of pydantic.
        orm_mode = True  # includes relationship data


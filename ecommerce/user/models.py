from sqlalchemy import Column, Integer, String

from ecommerce.db import Base
from .hashing import verify_password, get_password_hash


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255))

    def __int__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email

    def check_password(self, password):
        return verify_password(self.password, password)

    def set_password(self, password):
        self.password = get_password_hash(password)

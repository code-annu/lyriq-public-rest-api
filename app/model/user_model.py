from pydantic import BaseModel
from enum import Enum


class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'


class User(BaseModel):
    uid: str
    email: str
    role: str = UserRole.USER.value

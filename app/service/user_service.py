from app.repository.user_repository import UserRepository
from app.model.user_model import *


class UserService:
    _user_repository = UserRepository()

    def get_user(self, uid: str) -> User:
        return self._user_repository.get_user(uid)

    def create_new_user(self, user: User) -> User:
        return self._user_repository.create_new_user(user)

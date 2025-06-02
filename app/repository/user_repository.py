from app.core.exceptions import NotFoundException
from app.model.user_model import User
from app.core.database import get_user_collection


class UserRepository:
    _user_collection = get_user_collection()

    # Get user by uid
    def get_user(self, uid: str) -> User:
        user_dict = self._user_collection.find_one({"uid": uid})
        if user_dict:
            return User(**user_dict)
        raise NotFoundException(message="User not found")

    def create_new_user(self, user: User) -> User:
        user_dict = user.model_dump()
        self._user_collection.insert_one(user_dict)
        return user

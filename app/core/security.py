import os
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import auth as firebase_auth
from app.core.exceptions import NotFoundException
from app.service.user_service import UserService
from app.model.user_model import User, UserRole

load_dotenv()

# firebase_credentials = credentials.Certificate({
#     "type": "service_account",
#     "project_id": os.environ["FIREBASE_PROJECT_ID"],
#     "private_key": os.environ["FIREBASE_PRIVATE_KEY"].replace("\\n", "\n"),
#     "client_email": os.environ["FIREBASE_CLIENT_EMAIL"],
#     "token_uri": "https://oauth2.googleapis.com/token"
# })

firebase_credentials = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "token_uri": "https://oauth2.googleapis.com/token"
})

firebase_admin.initialize_app(firebase_credentials)

auth_scheme = HTTPBearer()  # defines the HTTP Bearer auth scheme
_user_service = UserService()


def get_current_user(auth_credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
    token = auth_credentials.credentials
    try:
        decoded_token = firebase_auth.verify_id_token(token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    uid = decoded_token.get("uid")
    email = decoded_token.get("email")
    try:
        user = _user_service.get_user(uid)
    except NotFoundException:
        user = _user_service.create_new_user(User(uid=uid, email=email))
    return user


def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != UserRole.ADMIN.value:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return current_user

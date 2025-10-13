from typing import Annotated
from fastapi import (
    APIRouter,
    Depends,
)

from api.api_v1.fastapi_users_router import (
    current_active_user,
    current_active_superuser,
)

from core.schemas.user import UserRead
from core.models.user import User
from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"]
)


@router.get("")
def get_user_messages(
    user: Annotated[
        User,
        Depends(current_active_user),
    ]
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[
        User,
        Depends(current_active_superuser)
    ]
):
    return {
        "messages": ["s-m1", "s-m2", "s-m3"],
        "user": UserRead.model_validate(user),
    }
from typing import Annotated
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user import User
from core.schemas.user import UserCreate, UserRead
from core.models import db_helper
from crud.users import get_all_users, create_user as create_users_crud


router = APIRouter(tags=["Users"])


@router.get(
    "",
    response_model=list[UserRead],
)
async def get_users(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
):
    users = await get_all_users(session=session)

    return users


@router.post(
    "",
    response_model=UserRead,
)
async def create_user(
    user_create: UserCreate,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> User:
    user = await create_users_crud(
        session=session,
        user_create=user_create,
    )

    return user

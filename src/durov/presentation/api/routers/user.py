from fastapi import APIRouter, Path, Depends, HTTPException, status

from durov.app.exceptions.user import UserNotFound
from durov.app.services.user import UserServiceInterface
from durov.presentation.api.dependencies.user import get_user_service
from durov.presentation.api.schemas.user import User, UserRegisteringRequest

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", summary="Register user", response_model=User)
async def register_user(
    data: UserRegisteringRequest,
    user_service: UserServiceInterface = Depends(get_user_service),
):
    """
    Registers user
    :param user_service: Initialized `UserService`
    :param data: A data for creating user
    :return: Created user
    """

    created_user = await user_service.register_user(
        data.to_dto(),
    )

    return created_user


@router.get(
    "/{nickname}",
    summary="Get user",
    description="Get user by it's nickname",
    response_model=User,
    responses={404: {"description": "User not found."}},
)
async def get_user(
    nickname: str = Path(
        title="Nickname", description="A nickname of user", examples=["Durov"]
    ),
    user_service: UserServiceInterface = Depends(get_user_service),
):
    """
    Returns a user by its nickname
    :param nickname: A nickname
    :param user_service: Initialized `UserService` object
    :return: User, ex: Pavel Durov.
    """
    try:
        user = await user_service.get_user_by_nickname(
            nickname,
        )
    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )

    return user

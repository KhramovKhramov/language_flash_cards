from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, status

from src.application.dto.user import UserCreateCommand
from src.application.use_cases.user.user_create import UserCreateUseCase
from src.entrypoints.api.user.schemas import (
    UserCreateRequestSchema,
    UserResponseSchema,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Creating new user",
    response_model=UserResponseSchema,
)
@inject
async def create_user(
    request_data: UserCreateRequestSchema,
    use_case: FromDishka[UserCreateUseCase],
):
    user_create_command: UserCreateCommand = UserCreateCommand(
        first_name=request_data.first_name,
        last_name=request_data.last_name,
        date_of_birth=request_data.date_of_birth,
        gender=request_data.gender,
        email=request_data.email,
    )

    return await use_case.execute(data=user_create_command)

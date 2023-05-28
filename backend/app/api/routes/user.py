from fastapi import APIRouter, Depends, HTTPException, status
from app.api.services.user_service import UserService, get_user_service
from app.api.schemas.user_schema import UserInput
from app.api.schemas.message_schema import StandardOutput, ErrorOutput
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends


user_router = APIRouter(prefix="/user")


@user_router.post(
    "/create_user",
    description="My description",
    response_model=StandardOutput,
    responses={400: {"model": ErrorOutput}},
)
async def create_user(
    user_input: UserInput, service: UserService = Depends(get_user_service)
):
    try:
        user = service.create_user(
            username=user_input.username, password=user_input.password
        )
        service.create_user_on_db(user=user)
        return StandardOutput(message="Ok user created")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.post(
    "/delete_user",
    description="My description",
    response_model=StandardOutput,
    responses={400: {"model": ErrorOutput}},
)
async def create_user(user_id: int, service: UserService = Depends(get_user_service)):
    try:
        service.delete_user_on_db(user_id=user_id)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.post(
    "/login", description="My description", responses={400: {"model": ErrorOutput}}
)
async def login(
    user_input: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(get_user_service),
):
    try:
        user_db = service.get_username(username=user_input.username)
        input_password = user_input.password
        hashed_password = user_db.password

        if not user_db or not user_db.password:
            raise HTTPException(
                status_code=401, detail="Incorrect username or password"
            )
        verified = service.validate_password(
            input_password=input_password, hashed_password=hashed_password
        )
        if not verified:
            raise HTTPException(
                status_code=401, detail="Incorrect username or password"
            )

        access_token = service.create_access_token(
            username=user_input.username, expire_in=30
        )
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.get("/ok")
def ok():
    return {"message": "Ok"}

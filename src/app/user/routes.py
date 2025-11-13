from fastapi import APIRouter
from .service.user import UserService


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

user_service = UserService()


@router.get("/")
async def read_users():
    return await user_service.get_user_count()
    

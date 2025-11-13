from src.core.artifacts.decorator import connect_db
from src.db.models import User
from sqlalchemy import select,func

class UserRepository:
    
    @connect_db()
    async def fetch_user_count(self,session) -> int:
        result = await session.execute(select(func.count()).select_from(User))
        return result.scalar_one()
from src.core.artifacts.interface.service import IService
from src.db.repository.user import UserRepository

class UserService(IService,UserRepository):
    service_name = "UserService"
    
    async def describe(self) -> str:
        return "Handling user related operations"
    
    async def get_user_count(self) -> int:
        # Placeholder for actual user count retrieval logic
        return await self.fetch_user_count()
        

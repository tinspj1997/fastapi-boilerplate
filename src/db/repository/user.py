from src.core.artifacts.decorator import connect_db


class UserRepository:
    
    @connect_db(commit=False)
    async def fecth_user_count(self,session) -> int:
        print(session)
        # Placeholder for actual database interaction
        return 42
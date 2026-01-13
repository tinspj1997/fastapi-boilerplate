from src.core.artifacts.decorator.db import inject_db
from src.core.artifacts.interface.repository import IReposiitory
from src.db.models import User
from sqlalchemy import select, func
from sqlalchemy.orm import Session


class UserRepository(IReposiitory):
    repository_name = "UserRepository"

    @inject_db()
    async def fetch_user_count(self, session: Session) -> int:
        result = session.execute(
            select(func.count()).select_from(User)
        )
        return result.scalar_one()

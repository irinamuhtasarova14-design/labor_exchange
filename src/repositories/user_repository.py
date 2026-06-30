from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from storage.sqlalchemy.tables import User
from models.dto.user_dto import UserDTO, UserCreateDTO, UserUpdateDTO

class UserRepository(
    BaseAlchemyGenericAsyncRepository[User, UserDTO, UserCreateDTO, UserUpdateDTO] # noqa
):
    alchemy_model = User
    output_model = UserDTO

    async def get_by_email(self, email: str) -> UserDTO | None:
        return await self.retrieve(email=email)

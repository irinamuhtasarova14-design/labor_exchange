from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from repositories.user_repository import UserRepository
from storage.sqlalchemy.tables import User
from models.dto.user_dto import UserDTO, UserCreateDTO, UserUpdateDTO

class UserUOW(AlchemyAsyncGenericUOW[User, UserDTO, UserCreateDTO, UserUpdateDTO]):
    repository: UserRepository
    pass
import bcrypt
from bases.services.base_service import BaseService
from uows.user_uow import UserUOW
from models.dto.user_dto import UserCreateDTO, UserDTO
from services.exceptions import ObjectExistsException, ObjectDoesntExistsException


class UserService(BaseService):
    def __init__(self, uow: UserUOW) -> None:
        self.uow = uow

    def _hash_password(self, password: str) -> str:
        """Хеширует пароль с помощью bcrypt."""
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(pwd_bytes, salt)
        return hashed_password.decode('utf-8')

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Сравнивает чистый пароль с хешем из базы данных."""
        password_bytes = plain_password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_password_bytes)

    async def register_user(self, user_in: UserCreateDTO) -> UserDTO:
        """Регистрация нового пользователя."""
        existing = await self.uow.repository.get_by_email(user_in.email)
        if existing:
            raise ObjectExistsException("Пользователь с таким email уже существует")
        hashed_password = self._hash_password(user_in.password)
        create_dto = user_in.model_copy(update={"password": hashed_password})

        async with self.uow as uow:
            new_user = await uow.repository.create(create_dto)
            await uow.commit()
            return new_user

    async def get_user_by_id(self, user_id: int) -> UserDTO:
        """Получение пользователя по ID."""
        user = await self.uow.repository.retrieve(id=user_id)
        if not user:
            raise ObjectDoesntExistsException(f"Пользователь с id={user_id} не найден")
        return user

    async def get_user_by_email(self, email: str) -> UserDTO:
        """Получение пользователя по email."""
        user = await self.uow.repository.get_by_email(email)
        if not user:
            raise ObjectDoesntExistsException(f"Пользователь с email={email} не найден")
        return user

    async def authenticate_user(self, email: str, password: str) -> UserDTO | None:
        """
        Аутентификация пользователя. Возвращает DTO, если всё верно, иначе None.
        """
        user = await self.uow.repository.get_by_email(email)
        if not user:
            return None
        if not self.verify_password(password, user.hashed_password):
            return None
        return user
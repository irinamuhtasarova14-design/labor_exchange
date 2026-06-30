from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from storage.sqlalchemy.tables import Response
from models.dto.response_dto import ResponseDTO, ResponseCreateDTO, ResponseUpdateDTO

class ResponseUOW(AlchemyAsyncGenericUOW[Response, ResponseDTO, ResponseCreateDTO, ResponseUpdateDTO]):
    pass
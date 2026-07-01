from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from storage.sqlalchemy.tables import Response
from models.dto.response_dto import ResponseDTO, ResponseCreateDTO, ResponseUpdateDTO


class ResponseRepository(
    BaseAlchemyGenericAsyncRepository[Response, ResponseDTO, ResponseCreateDTO, ResponseUpdateDTO] # noqa
):
    alchemy_model = Response
    output_model = ResponseDTO


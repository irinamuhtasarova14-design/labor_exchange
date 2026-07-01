from bases.services.base_service import BaseService
from uows.job_uow import JobUOW
from uows.response_uow import ResponseUOW
from models.dto.response_dto import ResponseCreateDTO, ResponseDTO
from services.exceptions import ObjectDoesntExistsException, SystemLogicError, NoPermissionException
from models.enums import UserRole

class ResponseService(BaseService):
    def __init__(self, response_uow: ResponseUOW, job_uow: JobUOW) -> None:
        self.response_uow = response_uow
        self.job_uow = job_uow

    async def response_job(self, response_create_data: ResponseCreateDTO, current_user_id: int, current_user_role: str) -> ResponseDTO:
        if current_user_role != UserRole.APPLICANT:
            raise NoPermissionException("Только соискатели могут откликаться на вакансии")

        async with self.job_uow as job_uow:
            job = await job_uow.repository.retrieve(id=response_create_data.job_id)
            if not job:
                raise ObjectDoesntExistsException("Вакансия не найдена")
            if not job.is_active:
                raise SystemLogicError("Нельзя откликнуться на неактивную вакансию")
        create_dto = response_create_data.model_copy(update={"user_id": current_user_id})

        async with self.response_uow as response_uow:
            response = await response_uow.repository.create(create_dto)
            await response_uow.commit()
            return response

    async def get_responses_by_job_id(self, job_id: int, current_user_id: int) -> list[ResponseDTO]:
        async with self.job_uow as job_uow:
            job = await job_uow.repository.retrieve(id=job_id)
            if job is None:
                raise ObjectDoesntExistsException("Вакансия не найдена")
            if job.user_id != current_user_id:
                raise NoPermissionException("Вы не являетесь владельцем этой вакансии")

        async with self.response_uow as response_uow:
            responses = await response_uow.repository.list(job_id=job_id)
            return list(responses)
from bases.services.base_service import BaseService
from uows.response_uow import ResponseUOW
from uows.job_uow import JobUOW
from models.dto.response_dto import ResponseCreateDTO, ResponseDTO
from services.exceptions import ObjectDoesntExistsException, NoPermissionException
from models.enums import UserRole


class ResponseService(BaseService):
    def __init__(self, response_uow: ResponseUOW, job_uow: JobUOW):
        self.response_uow = response_uow
        self.job_uow = job_uow

    async def create_response(self, response_create_data: ResponseCreateDTO, current_user_id: int, current_user_role: str) -> ResponseDTO:
        if current_user_role != UserRole.APPLICANT:
            raise NoPermissionException("Only applicants can respond to jobs")

        job = await self.job_uow.repository.retrieve(id=response_create_data.job_id)
        if not job:
            raise ObjectDoesntExistsException(f"Job with id {response_create_data.job_id} not found")

        create_dto = response_create_data.model_copy(update={"user_id": current_user_id})

        async with self.response_uow as uow:
            response = await uow.repository.create(create_dto)
            await uow.commit()
            return response

    async def get_responses_for_job(self, job_id: int, current_user_id: int) -> list[ResponseDTO]:
        job = await self.job_uow.repository.retrieve(id=job_id)
        if not job:
            raise ObjectDoesntExistsException(f"Job with id {job_id} not found")
        if job.user_id != current_user_id:
            raise NoPermissionException("You are not the owner of this job")

        async with self.response_uow as uow:
            return await uow.repository.list(job_id=job_id)

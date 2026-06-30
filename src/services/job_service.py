from bases.services.base_service import BaseService
from uows.job_uow import JobUOW
from models.dto.job_dto import JobCreateDTO, JobDTO
from services.exceptions import ObjectDoesntExistsException, NoPermissionException
from models.enums import UserRole


class JobService(BaseService):
    def __init__(self, uow: JobUOW) -> None:
        self.uow = uow

    async def create_job(self, job_create_data: JobCreateDTO, current_user_id: int, current_user_role: str) -> JobDTO:
        if current_user_role != UserRole.EMPLOYER:
            raise NoPermissionException("Только работодатели могут создавать вакансии")
        create_dto = job_create_data.model_copy(update={"user_id": current_user_id})
        async with self.uow as uow:
            job = await uow.repository.create(create_dto)
            await uow.commit()
            return job

    async def get_all_jobs(self, limit: int = 100, skip: int = 0) -> list[JobDTO]:
        async with self.uow as uow:
            jobs = await uow.repository.list(limit=limit, skip=skip)
            return list(jobs)

    async def get_job_by_id(self, job_id: int) -> JobDTO:
        async with self.uow as uow:
            job = await uow.repository.retrieve(id=job_id)
            if not job:
                raise ObjectDoesntExistsException(f"Вакансия с id={job_id} не найдена")
            return job

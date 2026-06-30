from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from storage.sqlalchemy.tables import Job
from models.dto.job_dto import JobDTO, JobCreateDTO, JobUpdateDTO


class JobRepository(
    BaseAlchemyGenericAsyncRepository[Job, JobDTO, JobCreateDTO, JobUpdateDTO] # noqa
):
    alchemy_model = Job
    output_model = JobDTO

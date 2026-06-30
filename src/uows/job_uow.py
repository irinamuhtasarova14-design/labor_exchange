from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from storage.sqlalchemy.tables import Job
from models.dto.job_dto import JobCreateDTO, JobDTO, JobUpdateDTO

class JobUOW(AlchemyAsyncGenericUOW[Job, JobDTO, JobCreateDTO, JobUpdateDTO]):
    pass
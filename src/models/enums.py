from enum import Enum

class UserRole(str, Enum):
    EMPLOYER = "employer"
    APPLICANT = "applicant"

class ResponseStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
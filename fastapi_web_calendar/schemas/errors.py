from pydantic import BaseModel


class BaseErrorResponse(BaseModel):
    message: dict

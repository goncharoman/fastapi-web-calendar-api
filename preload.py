from pydantic import BaseModel, validator


class CustomModel(BaseModel):
    event: str

    @validator("event", always=True, pre=True)
    def event_validator(cls, value):
        print(value)
        return value

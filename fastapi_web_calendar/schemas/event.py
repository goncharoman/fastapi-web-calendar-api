import datetime
from typing import Optional

from pydantic import BaseModel


class ResponseBase(BaseModel):
    """Base class of responses."""
    message: str


class EventBase(BaseModel):
    """Base class of shared properties."""
    event: Optional[str] = None
    date: Optional[datetime.date] = None


class EventCreate(EventBase):
    """Class of properties to receive on event creation."""
    event: str
    date: datetime.date


class EventUpdate(EventBase):
    pass


class EventInDBBase(EventBase):
    """Base class of properties shared by models stored in DB."""
    id: int
    event: str
    date: datetime.date

    class Config:
        orm_mode = True


class Event(EventInDBBase):
    """Class of properties to return in response."""
    pass


class EventRespose(ResponseBase):
    """Class of response for event methods."""
    event: Optional[Event] = None

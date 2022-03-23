import datetime
import enum
from typing import List, Optional

from fastapi import APIRouter, HTTPException, status
from fastapi_web_calendar import schemas

router = APIRouter()

FAKEDATA = {
    1: {"event": "Stand up", "date": datetime.date(2022, 3, 12)}
}
NEXT_ID = 2


@router.get("/", response_model=List[schemas.Event])
def read_events(start_time: Optional[str] = None, end_time: Optional[str] = None):
    events = FAKEDATA.items()
    if start_time:
        events = filter(lambda e: e[1]["date"] >= start_time, events)
    if end_time:
        events = filter(lambda e: e[1]["date"] <= end_time, events)
    return [dict(id=id, **event_data) for id, event_data in events]


@router.get("/today", response_model=List[schemas.Event])
def read_events_for_today():
    return list(filter(lambda e: e[1]["date"] == datetime.date.today(), FAKEDATA.items()))


@router.get("/{event_id}", response_model=schemas.Event)
def read_event_by_event_id(event_id: int):
    event = FAKEDATA.get(event_id)
    if not event:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return dict(id=event_id, **event)


@router.post("/", response_model=schemas.EventRespose, status_code=status.HTTP_201_CREATED)
def create_event(event: schemas.EventCreate):
    global NEXT_ID
    FAKEDATA[NEXT_ID] = event.dict()
    NEXT_ID += 1
    return {"message": "Event create.", "event": dict(id=NEXT_ID-1, **FAKEDATA[NEXT_ID-1])}


@router.patch("/{event_id}", response_model=schemas.EventRespose)
def update_event(event_id: int, event: schemas.EventUpdate):
    FAKEDATA[event_id].update(event.dict(exclude_unset=True))
    return {"message": "Event updated.", "event": dict(id=event_id, **FAKEDATA[event_id])}


@router.delete("/{event_id}", response_model=schemas.EventRespose)
def delete_event(event_id: int):
    event = FAKEDATA.pop(event_id)
    return {"message": "Event deleted.", "event": dict(id=event_id, **event)}

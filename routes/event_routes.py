from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import engine
from models.event import Event
from models.venue import Venue
from schemas.event_schema import EventCreate, EventResponse, EventUpdate
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EventResponse, status_code=201)
def create_event(event: EventCreate, db: Session = Depends(get_db)):

    venue = db.query(Venue).filter(Venue.id == event.venue_id).first()

    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")

    new_event = Event(
        venue_id=event.venue_id,
        name=event.name,
        description=event.description,
        event_date=event.event_date,
        capacity=event.capacity
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event

@router.get("/", response_model=list[EventResponse])
def get_all_events(
    skip: int = 0,
    limit: int = 10,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Event)

    if name:
        query = query.filter(Event.name.ilike(f"%{name}%"))

    events = query.offset(skip).limit(limit).all()

    return events

@router.get("/{event_id}", response_model=EventResponse)
def get_event_by_id(event_id: int, db: Session = Depends(get_db)):

    event = db.query(Event).filter(Event.id == event_id).first()

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    return event
@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event_data: EventUpdate, db: Session = Depends(get_db)):

    event = db.query(Event).filter(Event.id == event_id).first()

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    venue = db.query(Venue).filter(Venue.id == event_data.venue_id).first()

    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")

    event.venue_id = event_data.venue_id
    event.name = event_data.name
    event.description = event_data.description
    event.event_date = event_data.event_date
    event.capacity = event_data.capacity

    db.commit()
    db.refresh(event)

    return event


@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):

    event = db.query(Event).filter(Event.id == event_id).first()

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    try:
        db.delete(event)
        db.commit()

        return {"message": "Event deleted successfully"}

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Cannot delete this event because registrations are linked to it."
        )

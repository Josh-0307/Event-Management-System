from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import engine
from models.registration import Registration
from models.event import Event
from models.attendee import Attendee
from models.venue import Venue

from schemas.registration_schema import (
    RegistrationCreate,
    RegistrationResponse,
    RegistrationUpdate
)

router = APIRouter(
    prefix="/registrations",
    tags=["Registrations"]
)


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RegistrationResponse, status_code=201)
def create_registration(
    registration: RegistrationCreate,
    db: Session = Depends(get_db)
):

    event = db.query(Event).filter(
        Event.id == registration.event_id
    ).first()

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    attendee = db.query(Attendee).filter(
        Attendee.id == registration.attendee_id
    ).first()

    if attendee is None:
        raise HTTPException(status_code=404, detail="Attendee not found")

    existing_registration = db.query(Registration).filter(
        Registration.event_id == registration.event_id,
        Registration.attendee_id == registration.attendee_id
    ).first()

    if existing_registration:
        raise HTTPException(
            status_code=409,
            detail="Attendee is already registered for this event"
        )

    new_registration = Registration(
        event_id=registration.event_id,
        attendee_id=registration.attendee_id,
        status=registration.status
    )

    db.add(new_registration)
    db.commit()
    db.refresh(new_registration)

    return new_registration
@router.get("/", response_model=list[RegistrationResponse])
def get_all_registrations(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    registrations = db.query(Registration).offset(skip).limit(limit).all()
    return registrations



@router.get("/details")
def get_registration_details(db: Session = Depends(get_db)):

    details = db.query(
        Event.name.label("event_name"),
        Attendee.name.label("attendee_name"),
        Venue.name.label("venue_name"),
        Registration.status
    ).join(
        Event, Registration.event_id == Event.id
    ).join(
        Attendee, Registration.attendee_id == Attendee.id
    ).join(
        Venue, Event.venue_id == Venue.id
    ).all()

    return [
        {
            "event_name": row.event_name,
            "attendee_name": row.attendee_name,
            "venue_name": row.venue_name,
            "status": row.status
        }
        for row in details
    ]

@router.get("/{registration_id}", response_model=RegistrationResponse)
def get_registration_by_id(
    registration_id: int,
    db: Session = Depends(get_db)
):
    registration = db.query(Registration).filter(
        Registration.id == registration_id
    ).first()

    if registration is None:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    return registration
@router.put("/{registration_id}", response_model=RegistrationResponse)
def update_registration(
    registration_id: int,
    registration_data: RegistrationUpdate,
    db: Session = Depends(get_db)
):
    registration = db.query(Registration).filter(
        Registration.id == registration_id
    ).first()

    if registration is None:
        raise HTTPException(status_code=404, detail="Registration not found")

    event = db.query(Event).filter(
        Event.id == registration_data.event_id
    ).first()

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    attendee = db.query(Attendee).filter(
        Attendee.id == registration_data.attendee_id
    ).first()

    if attendee is None:
        raise HTTPException(status_code=404, detail="Attendee not found")

    duplicate = db.query(Registration).filter(
        Registration.event_id == registration_data.event_id,
        Registration.attendee_id == registration_data.attendee_id,
        Registration.id != registration_id
    ).first()

    if duplicate:
        raise HTTPException(
            status_code=409,
            detail="Attendee is already registered for this event"
        )

    registration.event_id = registration_data.event_id
    registration.attendee_id = registration_data.attendee_id
    registration.status = registration_data.status

    db.commit()
    db.refresh(registration)

    return registration
@router.delete("/{registration_id}")
def delete_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):
    registration = db.query(Registration).filter(
        Registration.id == registration_id
    ).first()

    if registration is None:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    db.delete(registration)
    db.commit()

    return {"message": "Registration deleted successfully"}

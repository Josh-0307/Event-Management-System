from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import engine
from models.attendee import Attendee
from schemas.attendee_schema import AttendeeCreate, AttendeeResponse, AttendeeUpdate
router = APIRouter(
    prefix="/attendees",
    tags=["Attendees"]
)


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AttendeeResponse, status_code=201)
def create_attendee(attendee: AttendeeCreate, db: Session = Depends(get_db)):

    existing_attendee = db.query(Attendee).filter(
        Attendee.email == attendee.email
    ).first()

    if existing_attendee:
        raise HTTPException(status_code=409, detail="Email already registered")

    new_attendee = Attendee(
        name=attendee.name,
        email=attendee.email,
        phone=attendee.phone
    )

    db.add(new_attendee)
    db.commit()
    db.refresh(new_attendee)

    return new_attendee
@router.get("/", response_model=list[AttendeeResponse])
def get_all_attendees(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    attendees = db.query(Attendee).offset(skip).limit(limit).all()
    return attendees

@router.get("/{attendee_id}", response_model=AttendeeResponse)
def get_attendee_by_id(attendee_id: int, db: Session = Depends(get_db)):

    attendee = db.query(Attendee).filter(
        Attendee.id == attendee_id
    ).first()

    if attendee is None:
        raise HTTPException(status_code=404, detail="Attendee not found")

    return attendee

@router.put("/{attendee_id}", response_model=AttendeeResponse)
def update_attendee(
    attendee_id: int,
    attendee_data: AttendeeUpdate,
    db: Session = Depends(get_db)
):
    attendee = db.query(Attendee).filter(
        Attendee.id == attendee_id
    ).first()

    if attendee is None:
        raise HTTPException(status_code=404, detail="Attendee not found")

    existing_email = db.query(Attendee).filter(
        Attendee.email == attendee_data.email,
        Attendee.id != attendee_id
    ).first()

    if existing_email:
        raise HTTPException(status_code=409, detail="Email already registered")

    attendee.name = attendee_data.name
    attendee.email = attendee_data.email
    attendee.phone = attendee_data.phone

    db.commit()
    db.refresh(attendee)

    return attendee

@router.delete("/{attendee_id}")
def delete_attendee(attendee_id: int, db: Session = Depends(get_db)):

    attendee = db.query(Attendee).filter(
        Attendee.id == attendee_id
    ).first()

    if attendee is None:
        raise HTTPException(status_code=404, detail="Attendee not found")

    db.delete(attendee)
    db.commit()

    return {"message": "Attendee deleted successfully"}
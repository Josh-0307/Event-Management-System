
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from models.venue import Venue
from schemas.venue_schema import VenueCreate, VenueResponse, VenueUpdate
from auth.dependencies import get_current_user, get_current_admin
router = APIRouter(
    prefix="/venues",
    tags=["Venues"]
)


@router.post("/", response_model=VenueResponse, status_code=201)
def create_venue(
    venue: VenueCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin)
):
    new_venue = Venue(
        name=venue.name,
        address=venue.address,
        city=venue.city,
        capacity=venue.capacity
    )

    db.add(new_venue)
    db.commit()
    db.refresh(new_venue)

    return new_venue


@router.get("/", response_model=list[VenueResponse])
def get_all_venues(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    venues = db.query(Venue).offset(skip).limit(limit).all()
    return venues


@router.get("/{venue_id}", response_model=VenueResponse)
def get_venue_by_id(
    venue_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    venue = db.query(Venue).filter(Venue.id == venue_id).first()

    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")

    return venue


@router.put("/{venue_id}", response_model=VenueResponse)
def update_venue(
    venue_id: int,
    venue_data: VenueUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin)
):
    venue = db.query(Venue).filter(Venue.id == venue_id).first()

    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")

    venue.name = venue_data.name
    venue.address = venue_data.address
    venue.city = venue_data.city
    venue.capacity = venue_data.capacity

    db.commit()
    db.refresh(venue)

    return venue


@router.delete("/{venue_id}")
def delete_venue(
    venue_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin)
):
    venue = db.query(Venue).filter(Venue.id == venue_id).first()

    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")

    db.delete(venue)
    db.commit()

    return {"message": "Venue deleted successfully"}

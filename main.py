
from fastapi import FastAPI
from routes.venue_routes import router as venue_router
from routes.event_routes import router as event_router
from routes.attendee_routes import router as attendee_router
from routes.registration_routes import router as registration_router
app = FastAPI(
    title="Event Management System",
    description="Backend API for managing venues, events, attendees and registrations",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Event Management System API!"
    }


# Register Venue API routes
app.include_router(venue_router)
app.include_router(event_router)
app.include_router(attendee_router)
app.include_router(registration_router)
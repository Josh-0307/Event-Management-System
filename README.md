# Event Management System

A Full-Stack Web Application for Managing Venues, Events, Attendees, and Registrations.


 1. Project Overview

The **Event Management System** is a web-based application developed to simplify and organize event management activities. It provides a centralized platform for managing venues, creating events, maintaining attendee information, and handling event registrations.

The application uses FastAPI for backend development, PostgreSQL for database management, and HTML, CSS, and JavaScript for the frontend.

It provides RESTful APIs, data validation, pagination, search functionality, and an interactive dashboard.

 2. Objectives

- To simplify venue and event management.
- To maintain attendee information efficiently.
- To manage event registrations systematically.
- To establish proper relationships between database tables.
- To provide reliable REST API operations.
- To display combined registration information through database joins.

 3. Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Database | PostgreSQL |
| API Documentation | Swagger UI |
| Development Environment | Visual Studio Code |
| Version Control | Git and GitHub |

 4. Features

 Dashboard
- Overview of venues, events, attendees, and registrations.
- Interactive dashboard cards.
- Navigation between management modules.

 Venue Management
- Add new venues.
- View all venues.
- Update venue information.
- Delete venues.

 Event Management
- Create and manage events.
- Associate events with venues.
- Search events by name.
- View and update event information.

 Attendee Management
- Add attendee details.
- View attendee records.
- Update attendee information.
- Delete attendee records.
- Validate email addresses.

Registration Management
- Register attendees for events.
- View registration records.
- Update registration status.
- Delete registrations.
- Prevent duplicate registrations.

 Registration Details
- Display registration information using database joins.
- Show event names, attendee names, and venue names.

 5. Database Design

The application uses PostgreSQL with four main tables.


venues : Stores venue details 
events : Stores event details and venue references 
attendees : Stores attendee information 
registrations : Stores event-attendee registration details 

 Entity Relationships

- One venue can have multiple events (One-to-Many).
- One event can have multiple registrations (One-to-Many).
- One attendee can have multiple registrations (One-to-Many).
- Events and attendees have a Many-to-Many relationship through the registrations table.

Database Constraints

- Primary key constraints.
- Foreign key constraints.
- NOT NULL constraints.
- Unique email constraint for attendees.
- Unique event-attendee combination in registrations.
- Timestamp fields for record tracking.

6. Business Rules

1. An attendee cannot register for the same event more than once.
2. Duplicate registrations return HTTP 409 Conflict.
3. Events with existing registrations cannot be deleted until their linked registrations are removed.
4. Event and attendee references must exist before a registration can be created.

7. API Functionalities

The application provides RESTful API operations for all four modules.

| HTTP Method | Operation | Description |
|---|---|---|
| POST | Create | Add a new record |
| GET | Read | Retrieve records |
| GET | Read by ID | Retrieve a specific record |
| PUT/PATCH | Update | Modify an existing record |
| DELETE | Delete | Remove a record |

Additional API functionalities:
- Event search by name.
- Pagination using `skip` and `limit`.
- Joined registration details.

8. HTTP Status Codes

| Status Code | Description |
|---|---|
| 200 | Successful request |
| 201 | Record created successfully |
| 400 | Invalid request |
| 404 | Requested record not found |
| 409 | Conflict or duplicate registration |

9. Project Structure

```text
EventManagementSystem/
│
├── database/
│   ├── base.py
│   └── connection.py
│
├── models/
│
├── schemas/
│
├── routes/
│
├── frontend/
│   └── index.html
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

10. Installation and Setup

Prerequisites

- Python 3.x
- PostgreSQL
- Visual Studio Code
- Git

Step 1: Clone the Repository

```bash
git clone https://github.com/Josh-0307/Event-Management-System.git
cd Event-Management-System
```

Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Step 3: Install Dependencies


pip install fastapi uvicorn sqlalchemy "psycopg[binary]" pydantic-settings python-dotenv email-validator


Step 4: Configure Environment Variables

Create a `.env` file in the project root and configure your PostgreSQL database connection settings.

Do not upload your `.env` file or database credentials to GitHub.

Step 5: Run the Application


uvicorn main:app --reload


11. Application Access

Once the server is running, access the application using the following URLs:

Application URL 

Frontend Dashboard : http://127.0.0.1:8000/app 
API Documentation : http://127.0.0.1:8000/docs 
Alternative API Documentation : http://127.0.0.1:8000/redoc 

12. Testing

The application can be tested using Swagger UI.

Testing includes:
- Creating, retrieving, updating, and deleting records.
- Validating required fields and email addresses.
- Checking foreign key relationships.
- Testing event search and pagination.
- Verifying duplicate registration prevention.
- Checking appropriate HTTP response codes.
- Testing joined registration details.

13. Future Enhancements

- User authentication and role-based access.
- Event booking notifications.
- Advanced event filtering.
- Report generation.
- Exporting registration details.

14. Conclusion

The Event Management System demonstrates the development of a full-stack web application using FastAPI, PostgreSQL, and frontend technologies.

It provides an organized approach to managing venues, events, attendees, and registrations while implementing database relationships, validation, business rules, and RESTful API functionality.



Project Name: Event Management System  
Backend: Python – FastAPI  
Database: PostgreSQL  
Frontend: HTML, CSS, JavaScript  
Repository: https://github.com/Josh-0307/Event-Management-System
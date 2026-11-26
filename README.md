# Event Management System

A full-stack Event Management System designed to simplify the management of venues, events, attendees, and registrations. The application provides a RESTful API powered by FastAPI, a PostgreSQL database, and an interactive web-based dashboard.

The system implements JWT-based authentication and Role-Based Access Control (RBAC), providing separate permissions for regular users and administrators.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [User Roles and Permissions](#user-roles-and-permissions)
- [API Documentation](#api-documentation)
- [Authentication and Security](#authentication-and-security)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)

---

## Overview

The Event Management System is a web application that provides a centralized platform for managing event-related operations.

It enables administrators to manage venues, events, attendees, and registrations, while regular users can securely access and view available information.

The application follows a modular backend architecture, separating database operations, data models, validation schemas, authentication, and API routes.

## Key Features

### Authentication and Authorization
- User registration and login.
- JWT-based authentication.
- Secure password hashing using Argon2.
- Protected API endpoints.
- Role-Based Access Control (RBAC).
- Automatic token validation and expiration handling.

### Venue Management
- Create and manage venue records.
- View venue information.
- Update venue details.
- Delete venue records.
- Maintain venue address, city, and capacity information.

### Event Management
- Create and manage events.
- View event information.
- Update event details.
- Delete events.

### Attendee Management
- Manage attendee records.
- View attendee information.
- Perform administrative record management.

### Registration Management
- Manage event registrations.
- View registration records.
- Access registration details.

### Interactive Dashboard
- Dashboard statistics.
- Dedicated sections for each resource.
- Search and data table functionality.
- Add, edit, and delete interfaces.
- Dynamic form handling.
- Role-based interface restrictions.

---

## Technology Stack

| Category | Technologies |
|---|---|
| Backend | Python, FastAPI |
| Frontend | HTML5, CSS3, JavaScript |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Data Validation | Pydantic |
| Authentication | JWT, PyJWT |
| Password Security | pwdlib, Argon2 |
| API Testing | Postman |
| API Documentation | Swagger UI |
| Version Control | Git, GitHub |

---

## System Architecture

The application follows a layered architecture.

**Frontend Layer**

The HTML, CSS, and JavaScript-based interface communicates with the backend through HTTP requests.

**Backend Layer**

FastAPI handles:
- API routing and request processing.
- Authentication and authorization.
- Input validation.
- Business logic.
- Database interactions.

**Database Layer**

PostgreSQL stores application data, while SQLAlchemy provides database access and ORM functionality.

### Authentication Flow

1. A user registers or logs in.
2. The backend validates the submitted credentials.
3. The password is verified against its stored hash.
4. A JWT access token is generated after successful authentication.
5. The frontend includes the token in subsequent API requests.
6. The backend validates the token and identifies the authenticated user.
7. Role-based authorization determines whether the requested operation is permitted.

---

## Project Structure

```text
EventManagementSystem/
│
├── auth/
│   ├── dependencies.py
│   └── security.py
│
├── database/
│   ├── base.py
│   └── connection.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── ...
│
├── schemas/
│   ├── user.py
│   └── ...
│
├── routes/
│   ├── auth.py
│   ├── venue_routes.py
│   ├── event_routes.py
│   ├── attendee_routes.py
│   └── registration_routes.py
│
├── frontend/
│   └── index.html
│
├── POSTMAN/
│   └── Documentation.txt
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## User Roles and Permissions

The application implements two roles:

| Operation | USER | ADMIN |
|---|:---:|:---:|
| Login | ✓ | ✓ |
| View venues | ✓ | ✓ |
| View events | ✓ | ✓ |
| View attendees | ✓ | ✓ |
| View registrations | ✓ | ✓ |
| Create records | ✗ | ✓ |
| Update records | ✗ | ✓ |
| Delete records | ✗ | ✓ |

Administrative operations are protected at the backend level using role-based dependencies.

Frontend restrictions provide an additional user-interface layer but do not replace backend authorization.

---

## API Documentation

The application exposes RESTful API endpoints through FastAPI.

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate and obtain an access token |

### Venues

| Method | Endpoint | Description |
|---|---|---|
| GET | `/venues/` | Retrieve venues |
| POST | `/venues/` | Create a venue |
| PUT | `/venues/{venue_id}` | Update a venue |
| DELETE | `/venues/{venue_id}` | Delete a venue |

### Events

| Method | Endpoint | Description |
|---|---|---|
| GET | `/events/` | Retrieve events |
| POST | `/events/` | Create an event |
| PUT | `/events/{event_id}` | Update an event |
| DELETE | `/events/{event_id}` | Delete an event |

### Attendees

| Method | Endpoint | Description |
|---|---|---|
| GET | `/attendees/` | Retrieve attendees |
| POST | `/attendees/` | Create an attendee |
| PUT | `/attendees/{attendee_id}` | Update an attendee |
| DELETE | `/attendees/{attendee_id}` | Delete an attendee |

### Registrations

| Method | Endpoint | Description |
|---|---|---|
| GET | `/registrations/` | Retrieve registrations |
| POST | `/registrations/` | Create a registration |
| PUT | `/registrations/{registration_id}` | Update a registration |
| DELETE | `/registrations/{registration_id}` | Delete a registration |
| GET | `/registrations/details` | Retrieve registration details |

For complete request schemas, response formats, and endpoint specifications, refer to the interactive Swagger documentation.

---

## Authentication and Security

The application incorporates the following security mechanisms:

- **JWT Authentication:** Authenticates users through signed access tokens.
- **Password Hashing:** Uses Argon2 to securely hash passwords.
- **Role-Based Access Control:** Restricts administrative operations to ADMIN users.
- **Protected Routes:** Validates authentication before granting access to protected endpoints.
- **Environment Variables:** Stores sensitive configuration outside the source code.
- **Backend Authorization:** Enforces permissions independently of frontend controls.

---

## Installation and Setup

### Prerequisites

Ensure the following software is installed:

- Python 3.10 or later
- PostgreSQL
- Git
- Postman (for API testing)

### 1. Clone the Repository

```bash
git clone https://github.com/Josh-0307/Event-Management-System.git
```

Navigate into the project directory:

```bash
cd Event-Management-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database for the application.

### 5. Configure Environment Variables

Create a `.env` file in the project root.

Add the database connection and JWT configuration using the variable names expected by `database/connection.py` and `auth/security.py`.

Keep all credentials and secret keys private.

**Important:** Never commit your `.env` file to GitHub.

### 6. Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

---

## Running the Application

Once the server starts successfully, access the application through the following URLs:

| Resource | URL |
|---|---|
| Web Application | http://127.0.0.1:8000/app/ |
| Swagger API Documentation | http://127.0.0.1:8000/docs |
| ReDoc API Documentation | http://127.0.0.1:8000/redoc |

---

## Testing

API endpoints and access permissions are tested using **Postman**.

The authentication and authorization testing process includes:

- USER and ADMIN login verification.
- JWT-protected API access.
- USER read-access verification.
- USER write-operation restriction.
- ADMIN create-operation verification.
- ADMIN update-operation verification.
- ADMIN delete-operation verification.

Expected HTTP status codes include:

| Status Code | Meaning |
|---|---|
| 200 OK | Request successful |
| 201 Created | Resource successfully created |
| 403 Forbidden | User does not have permission |
| 401 Unauthorized | Authentication required or invalid |
| 404 Not Found | Requested resource does not exist |

Postman-related documentation is available in the `POSTMAN/` directory.

---

## Future Enhancements

Potential improvements for future versions include:

- Email notifications for event registrations.
- Event booking and payment integration.
- Advanced search and filtering.
- Enhanced dashboard analytics.
- Event scheduling and calendar integration.
- Cloud deployment.
- Automated unit and integration testing.

---

## License

This project is developed as an internship project. Licensing terms can be added as required.

---

## Author

**Event Management System**

GitHub Repository:  
https://github.com/Josh-0307/Event-Management-System

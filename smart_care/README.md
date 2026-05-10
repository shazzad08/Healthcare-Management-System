# Smart Care — Healthcare Management System

> A Django REST Framework–powered backend for managing patients, doctors, appointments, and hospital services.

---



## Overview

Smart Care is a RESTful backend system built to streamline healthcare operations. It handles patient registration and authentication, doctor profile management, appointment scheduling, medical service listings, and customer inquiries — all exposed through clean, well-structured API endpoints designed for seamless frontend integration.

---

##Tech Stack

Backend:

Django 5.2.10
Django REST Framework
Python 3.x

Database:

SQLite3 (Development)
PostgreSQL Ready (Production)

Authentication:

DRF Token Authentication

Additional Libraries:

django-filter
django-environ
Pillow
gunicorn


---

## Project Structure

```
smart_care/
├── appointment/          # Appointment scheduling logic
├── contact_us/           # Customer inquiry handling
├── doctor/               # Doctor profiles, reviews, availability
├── patient/              # Patient registration & auth
├── service/              # Hospital service listings
├── smart_care/           # Core project configuration
├── media/                # Uploaded images and documents
├── db.sqlite3            # Development database
├── manage.py
└── requirement.txt
```

---

## API Modules

### Patient

Handles user registration, email verification, login/logout, and profile management.

**Models:** `Patient` (extends Django `User` with phone and profile image)

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/patient/register/` | Register a new patient |
| `GET` | `/patient/active/<uid64>/<token>/` | Email verification |
| `POST` | `/patient/login/` | Authenticate and receive token |
| `GET` | `/patient/logout/` | Invalidate session token |
| `GET` | `/patient/list/` | List all patients (paginated) |
| `GET` | `/patient/list/<id>/` | Retrieve a specific patient |
| `PUT` | `/patient/list/<id>/` | Update patient profile |
| `DELETE` | `/patient/list/<id>/` | Remove patient record |

---

### Doctor

Manages doctor profiles including specializations, designations, available time slots, and patient reviews.

**Models:** `Specialization`, `Designation`, `AvailableTime`, `Doctor`, `Review`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/doctor/list/` | List doctors (paginated, searchable) |
| `GET` | `/doctor/list/<id>/` | Retrieve a specific doctor |
| `POST` | `/doctor/list/` | Create doctor profile |
| `PUT` | `/doctor/list/<id>/` | Update doctor profile |
| `DELETE` | `/doctor/list/<id>/` | Remove doctor profile |
| `GET` | `/doctor/specialization/` | List all specializations |
| `GET` | `/doctor/designation/` | List all designations |
| `GET` | `/doctor/availabletime/` | List available time slots |
| `POST` | `/doctor/review/` | Submit a review (auth required) |
| `GET` | `/doctor/review/` | List reviews (paginated, searchable) |

---

### Appointment

Manages the full lifecycle of appointments between patients and doctors.

**Models:** `Appointment` — supports Online/Offline types and Complete/Pending/Running statuses.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/appointment/appointment/` | List all appointments |
| `GET` | `/appointment/appointment/?patient_id=<id>` | Filter by patient |
| `GET` | `/appointment/appointment/?doctor_id=<id>` | Filter by doctor |
| `POST` | `/appointment/appointment/` | Book a new appointment |
| `PUT` | `/appointment/appointment/<id>/` | Update appointment details |
| `DELETE` | `/appointment/appointment/<id>/` | Cancel appointment |

---

### Service

Manages hospital service listings with descriptions and images.

**Models:** `Service`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/service/service/` | List all services |
| `POST` | `/service/service/` | Add a new service |
| `PUT` | `/service/service/<id>/` | Update a service |
| `DELETE` | `/service/service/<id>/` | Remove a service |

---

### Contact Us

Collects and stores patient/visitor inquiries.

**Models:** `ContactUs`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/contact_us/contact_us/` | List all inquiries |
| `POST` | `/contact_us/contact_us/` | Submit a new inquiry |
| `PUT` | `/contact_us/contact_us/<id>/` | Update an inquiry |
| `DELETE` | `/contact_us/contact_us/<id>/` | Delete an inquiry |

---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository and navigate to the project
cd smart_care

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirement.txt

# 4. Set up environment variables
#    Create a .env file in the project root:
EMAIL=your_gmail@gmail.com
EMAIL_PASSWORD=your_app_password

# 5. Apply database migrations
python manage.py migrate

# 6. Create an admin superuser
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.  
The admin panel is accessible at `http://127.0.0.1:8000/admin/`.

---

## Configuration

### Email (Gmail SMTP)

Used for patient email verification on registration. Set credentials in `.env`:

```
EMAIL=your_gmail@gmail.com
EMAIL_PASSWORD=your_app_password
```

### Database

- **Development:** SQLite3 (`db.sqlite3`) — default, no configuration needed.
- **Production:** PostgreSQL via `dj-database-url`. Update `DATABASES` in `settings.py` accordingly.

### Media Storage

| Content | Path |
|---|---|
| Patient profile images | `/media/patient/image/` |
| Doctor images | `/media/doctor/images/` |
| Service images | `/media/service/images/` |

---

## Authentication

Smart Care uses **Token-based Authentication** via Django REST Framework's `authtoken`.

1. Authenticate via `POST /patient/login/` to receive a token.
2. Include the token in the `Authorization` header of all subsequent requests:

```
Authorization: Token <your_token_here>
```

---

## API Reference

### Register a Patient

```http
POST /patient/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepass123",
  "password2": "securepass123",
  "first_name": "John",
  "last_name": "Doe"
}
```

### Login

```http
POST /patient/login/
Content-Type: application/json

{
  "username": "john_doe",
  "password": "securepass123"
}
```

### Book an Appointment

```http
POST /appointment/appointment/
Authorization: Token <your_token_here>
Content-Type: application/json

{
  "patient": 1,
  "doctor": 2,
  "symptom": "Headache and fever",
  "time": 1,
  "appointment_types": "Online",
  "appointment_status": "Pending"
}
```

### Search Doctors

```http
GET /doctor/list/?search=cardiology
GET /doctor/list/?search=Dr. Smith
```

---

## Data Model

```
User (Django Auth)
├── Patient (OneToOne)
│   ├── Appointment (ForeignKey)
│   └── Review (ForeignKey)
│
└── Doctor (OneToOne)
    ├── Specialization (ManyToMany)
    ├── Designation (ManyToMany)
    ├── AvailableTime (ManyToMany)
    ├── Appointment (ForeignKey)
    └── Review (ForeignKey)

Service      (standalone)
ContactUs    (standalone)
```

---

## Roadmap

- [ ] Prescription and medical records management
- [ ] Email/SMS appointment reminders
- [ ] Payment gateway integration
- [ ] Doctor availability calendar view
- [ ] Video consultation support
- [ ] Mobile application (iOS & Android)
- [ ] Advanced analytics and reporting dashboard

---

## License

This project is part of a Healthcare Management System. All rights reserved.


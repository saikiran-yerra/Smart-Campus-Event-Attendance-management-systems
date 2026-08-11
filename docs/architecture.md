# System Architecture

## Overview

The Smart Campus Event & Attendance Management System is a multi-tier web application with separation of concerns across frontend, backend, database, and AI recommendation service layers.

---

## High-Level System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     Frontend (Static HTML/JS)                   │
│              index.html, dashboard.html, events.html            │
│           login.html, register.html, attendance.html            │
└────────────────────────────┬────────────────────────────────────┘
                             │
                    HTTP/HTTPS Requests
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Flask Backend (REST API)                     │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                  Blueprint Routes                          │ │
│  │  ┌──────────────┬─────────────┬──────────────┬────────────┐ │
│  │  │   auth_api   │ events_api  │attendance_api│notification│ │
│  │  │              │             │              │_api        │ │
│  │  └──────────────┴─────────────┴──────────────┴────────────┘ │
│  │                                                              │
│  │  ┌────────────────────────────────────────────────────────┐ │
│  │  │        Core Services (Flask app.py modules)           │ │
│  │  │  ┌──────────┬────────┬──────────┬───────────────────┐  │
│  │  │  │ Database │ Email  │ User     │ Event Management  │  │
│  │  │  │ Service  │Service │ Service  │ Service           │  │
│  │  │  └──────────┴────────┴──────────┴───────────────────┘  │
│  │  │                                                         │
│  │  │  Configuration: Environment variables via .env         │
│  │  └────────────────────────────────────────────────────────┘ │
│  └────────────────────────────────────────────────────────────┘
└────────────┬──────────────────────────────────────┬────────────┘
             │                                      │
   SQL Queries & Data                   AI Requests (JSON)
             │                                      │
             ▼                                      ▼
┌─────────────────────────────┐  ┌────────────────────────────────┐
│     MySQL Database          │  │  AI Recommendation Service     │
│                             │  │                                │
│  ┌─────────────────────────┤  │  ┌──────────────────────────┐   │
│  │ users                   │  │  │ recommendation_engine.py │   │
│  │ events                  │  │  │ train_model.py           │   │
│  │ attendance              │  │  │ preprocess.py            │   │
│  │ notifications           │  │  │ utils.py                 │   │
│  │ attendances_history     │  │  │                          │   │
│  └─────────────────────────┤  │  ├──────────────────────────┤   │
│                             │  │  │ Model & Data             │   │
│                             │  │  │ model.pkl (trained)      │   │
│                             │  │  │ dataset.csv              │   │
│                             │  │  │ Features: scikit-learn   │   │
│                             │  │  └──────────────────────────┘   │
│                             │  │                                │
│  Schema: schema.sql         │  │  Tech: Scikit-learn, pandas,   │
│  Sample data: sample_data.sql │  │  numpy                       │
│                             │  │                                │
└─────────────────────────────┘  └────────────────────────────────┘
```

---

## Service Boundaries

### Frontend Service
- **Technology:** HTML5, CSS3, JavaScript
- **Responsibility:** User interface for students and administrators
- **Features:**
  - Event discovery and registration
  - Attendance tracking
  - User authentication
  - Dashboard with statistics
- **Files:** `frontend/` directory
- **Communication:** HTTP requests to Flask backend

### Backend Service (Flask)
- **Technology:** Python, Flask framework
- **Responsibility:** Core business logic, API endpoints, database management
- **Components:**
  - **Authentication API:** User login, registration, session management
  - **Events API:** CRUD operations for events
  - **Attendance API:** Mark attendance, generate reports
  - **Notifications API:** Send emails and notifications
  - **Recommendation API:** Integrate with AI service for personalized suggestions
- **Files:** `backend/` and `api/` directories
- **Communication:** 
  - Receives HTTP requests from frontend
  - Queries MySQL database
  - Calls AI recommendation service (JSON over HTTP)

### Database Service (MySQL)
- **Technology:** MySQL 5.7+ / 8.0
- **Responsibility:** Persistent data storage
- **Tables:**
  - `users` - User accounts and roles
  - `events` - Event details
  - `attendance` - Attendance records
  - `notifications` - Notification history
- **Files:** `database/` directory
- **Communication:** SQL queries from Flask backend

### AI Recommendation Service
- **Technology:** Python, Scikit-learn, Pandas, NumPy
- **Responsibility:** Personalized event recommendations
- **Features:**
  - Model training on historical attendance data
  - Event recommendation generation
  - Interest-based filtering
- **Files:** `ai_recommendation/` directory
- **Communication:** JSON endpoint called by recommendation_api.py

---

## Folder Structure & Purpose

```
smart-campus-system/
│
├── frontend/                    # Static web interface
│   ├── index.html              # Landing page
│   ├── login.html              # Authentication
│   ├── register.html           # User registration
│   ├── dashboard.html          # Main dashboard
│   ├── events.html             # Event listing
│   ├── attendance.html         # Attendance interface
│   ├── app.js                  # Client-side logic
│   └── style.css               # Styling
│
├── backend/                     # Flask REST API & core services
│   ├── app.py                  # Flask app initialization
│   ├── routes/                 # Blueprints (modular routes)
│   │   ├── auth.py             # Authentication routes
│   │   ├── events.py           # Event routes
│   │   ├── attendance.py       # Attendance routes
│   │   └── notifications.py    # Notification routes
│   ├── auth_service.py         # Auth business logic
│   ├── event.py                # Event models/service
│   ├── attendance.py           # Attendance service
│   ├── user.py                 # User models/service
│   ├── email_service.py        # Email notifications
│   ├── database.py             # Database connection
│   ├── config.py               # Local config
│   └── requirements.txt        # Backend dependencies
│
├── api/                         # External API integrations
│   ├── attendance_api.py       # Attendance endpoints
│   ├── auth_api.py             # Auth endpoints
│   ├── events_api.py           # Events endpoints
│   ├── notification_api.py     # Notification endpoints
│   ├── recommendation_api.py   # AI recommendation endpoints
│   └── routes.py               # Route aggregation
│
├── ai_recommendation/           # ML recommendation engine
│   ├── recommendation_engine.py # Inference logic
│   ├── train_model.py          # Model training
│   ├── preprocess.py           # Data preprocessing
│   ├── utils.py                # Utility functions
│   ├── dataset.csv             # Training data
│   ├── model.pkl               # Trained model (binary)
│   └── requirements.txt        # ML dependencies
│
├── config/                      # Configuration management
│   ├── app_settings.py         # General settings
│   ├── config.py               # Base config
│   ├── database_config.py      # Database settings
│   ├── email_config.py         # Email settings
│   ├── logging_config.py       # Logging setup
│   ├── security_config.py      # Security settings
│   ├── development.py          # Dev environment
│   └── production.py           # Prod environment
│
├── database/                    # Database schema & sample data
│   ├── schema.sql              # Table definitions
│   ├── users.sql               # User data setup
│   ├── events.sql              # Event data setup
│   ├── attendance.sql          # Attendance setup
│   ├── notifications.sql       # Notifications setup
│   └── sample_data.sql         # Test data
│
├── test/                        # Unit test suite
│   ├── test_auth.py            # Authentication tests
│   ├── test_events.py          # Event API tests
│   ├── test_attendance.py      # Attendance tests
│   ├── test_notifications.py   # Notification tests
│   ├── test_recommendation.py  # ML recommendation tests
│   └── test_database.py        # Database tests
│
├── docs/                        # Documentation
│   ├── architecture.md         # This file
│   └── cm-audit/               # Audit reports
│
├── .github/                     # GitHub-specific files
│   ├── workflows/
│   │   └── ci.yml              # CI/CD pipeline
│   ├── CODEOWNERS              # Review routing
│   ├── ISSUE_TEMPLATE/         # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md # PR template
│
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
├── README.md                    # Project overview
├── CONTRIBUTING.md             # Contribution guidelines
├── SECURITY.md                 # Security policy
├── CHANGELOG.md                # Version history
└── requirements-lock.txt       # Pinned dependencies
```

---

## Environment Configuration

The application requires the following environment variables (configured via `.env` file):

### Database Configuration
- `MYSQL_HOST` - Database server hostname (e.g., `localhost`)
- `MYSQL_USER` - Database user (e.g., `smart_campus`)
- `MYSQL_PASSWORD` - Database password
- `MYSQL_DB` - Database name (e.g., `smart_campus_db`)

### Flask Configuration
- `FLASK_SECRET_KEY` - Secret key for session management and CSRF protection
- `FLASK_ENV` - Environment mode (`development` or `production`)

### Optional
- `FLASK_DEBUG` - Debug mode flag
- `EMAIL_CONFIG` - Email service settings (if using email notifications)

**Never commit `.env` files.** Use `.env.example` as a template for local development.

---

## Data Flow

### 1. User Authentication
```
Student/Admin → Frontend (login.html)
                → Backend (POST /api/auth/login)
                → Verify credentials in MySQL
                → Return session token/JWT
                → Frontend stores token, grants access
```

### 2. Event Discovery & Registration
```
Frontend (events.html)
  → Backend (GET /api/events)
    → Query MySQL events table
    → Return event list
  → Display events to user
  → User selects event
  → Frontend (POST /api/events/{id}/register)
    → Backend inserts attendance record
    → Return confirmation
```

### 3. Event Recommendation
```
Backend (GET /api/recommendations)
  → Call AI service (recommendation_engine.py)
    → Load trained model (model.pkl)
    → Fetch user's attendance history from MySQL
    → Preprocess data (preprocess.py)
    → Predict recommendations
  → Return top N recommended events
  → Frontend displays suggestions
```

### 4. Attendance Marking
```
Admin/Student → Frontend (attendance.html)
                → Backend (POST /api/attendance/mark)
                  → Verify QR code / student ID
                  → Insert record into MySQL
                  → Send confirmation notification (email_service.py)
                → Return success
```

---

## Deployment Considerations

- **Development:** Run Flask in debug mode on `localhost:5000`, MySQL locally or via Docker
- **Production:** Use a WSGI server (e.g., Gunicorn), managed database (AWS RDS, Azure Database for MySQL), environment variables for secrets
- **CI/CD:** GitHub Actions runs tests on every push and PR
- **Database:** Initialize with `database/schema.sql` and optionally `sample_data.sql`
- **Model Updates:** Retrain recommendation model regularly using `ai_recommendation/train_model.py`

---

## Security Architecture

- **Authentication:** Username/password with encrypted session tokens
- **Database:** SQL queries use parameterized statements to prevent SQL injection
- **API:** Routes protected by authentication middleware
- **Secrets:** All credentials managed via environment variables, never hardcoded
- **HTTPS:** Recommended for production deployments

See [SECURITY.md](../SECURITY.md) for detailed security guidelines.

---

## Related Documentation

- [README.md](../README.md) - Project overview and setup instructions
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Development workflow
- [SECURITY.md](../SECURITY.md) - Security policies and best practices
- [CHANGELOG.md](../CHANGELOG.md) - Version history and release notes

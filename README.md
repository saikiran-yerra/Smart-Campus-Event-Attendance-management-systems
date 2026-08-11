# Smart Campus Event & Attendance Management System

## Overview

The Smart Campus Event & Attendance Management System is a web-based application designed to simplify event management in educational institutions. The system enables administrators to create events, manage student registrations, track attendance, send notifications, and generate analytics reports.

The project also includes an AI-powered recommendation engine that suggests events to students based on their interests.

---

## Features

### User Management

* User registration
* User login
* Role-based access control
* Student and administrator accounts

### Event Management

* Create events
* Update events
* Delete events
* View event details

### Attendance Management

* Mark attendance
* View attendance reports
* QR code attendance verification

### Notification System

* Email notifications
* SMS notifications
* Event reminders

### Analytics Dashboard

* Total events
* Student participation
* Attendance statistics
* Performance reports

### AI Recommendation Engine

* Personalized event recommendations
* Interest-based suggestions
* Machine learning model integration

---

## Architecture

For a detailed overview of the system architecture, including service boundaries, data flow, and component interactions, see [architecture.md](docs/architecture.md).

---

## Project Structure

smart-campus-system/

├── frontend/

├── backend/

├── database/

├── api/

├── ai-recommendation/

├── docs/

├── test/

├── config/

├── README.md

└── requirements.txt

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Database

* MySQL

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Version Control

* Git
* GitHub

---

## Installation

### Clone the repository

```bash
git clone https://github.com/username/smart-campus-system.git
```

### Move into the project directory

```bash
cd smart-campus-system
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Create the database:

```sql
CREATE DATABASE smart_campus;
```

Import the SQL files:

```bash
mysql -u root -p smart_campus < database/schema.sql
```

---

## Run the Backend Server

```bash
python backend/app.py
```

The server runs at:

```text
http://127.0.0.1:5000
```

---

## API Endpoints

### Authentication

POST /api/register

POST /api/login

### Events

GET /api/events

POST /api/events

DELETE /api/events/{id}

### Attendance

GET /api/attendance

POST /api/attendance

### Notifications

POST /api/notify

### Recommendations

GET /api/recommendations/{student_id}

---

## Running Tests

Run all tests:

```bash
python -m unittest discover -s test -p "test_*.py"
```

Run a single test:

```bash
python -m unittest test.test_auth
```

---

## Version Control Workflow

1. Create a feature branch.

```bash
git checkout -b feature-name
```

2. Commit changes.

```bash
git add .

git commit -m "Implemented new feature"
```

3. Push the branch.

```bash
git push origin feature-name
```

4. Create a pull request.

5. Merge into the main branch.

---

## Release Management

Create a release tag:

```bash
git tag -a v1.0 -m "Initial release"

git push origin v1.0
```

---

## Contributors

Sai Kiran Yerramaneni

---

## License

This project is developed for academic purposes only.

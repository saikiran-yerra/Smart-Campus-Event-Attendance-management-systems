# Product Requirements Document

## Smart Campus Event & Attendance Management System

---

## Cover Page

- Project Name: Smart Campus Event & Attendance Management System
- Student(s): Sai Kiran Yerramaneni
- Course: CISC 593/594
- Semester: To Be Completed
- Repository URL: https://github.com/saikiran-yerra/smart-campus-Event-Attendance-Management-System.git
- Current Branch: main
- Current Commit SHA: cffa152c1d8a016282a57fde720b948720516cd7
- Current Release Version: Version 1 / Version 2 roadmap; exact release numbers To Be Completed
- Document Version: 0.1
- Last Updated: 2026-07-21

---

## Revision History

| Version | Date | Git Commit | Description | Author |
|----------|------|------------|-------------|--------|
| 0.1 | 2026-07-21 | cffa152c1d8a016282a57fde720b948720516cd7 | Initial PRD drafted from the repository proposal, README, and prompt requirements | Sai Kiran Yerramaneni |

---

## Table of Contents

1. Product Vision
2. Product Scope
3. Software Capabilities
4. Undesirable Events
5. Risk Analysis
6. Risk Prioritization
7. Risk Mitigation
8. Functional Requirements
9. Quality Requirements
10. Performance Requirements
11. Assumptions
12. Constraints
13. External Interfaces

---

# 1. Product Vision

## Problem Statement

Educational institutions often rely on spreadsheets, paper attendance sheets, or standalone tools to organize workshops, seminars, technical events, and student activities. These approaches can create scheduling conflicts, inaccurate attendance tracking, ineffective communication, and reduced student involvement.

## Intended Users

The repository proposal identifies the following users:

- College administrators
- Faculty event coordinators
- Students
- Department heads

## Stakeholders

The primary stakeholders reflected in the repository are:

- Institution administrators
- Faculty coordinators
- Students
- Department leadership
- Repository maintainers and course instructors

## Product Goals

The system is intended to:

- Provide a centralized platform for campus event planning and coordination
- Support online event registration
- Track attendance reliably
- Improve communication through notifications and reminders
- Support event participation history and reporting
- Introduce intelligent recommendations in later development

## Major Features

The repository documents the following major features:

- User authentication and role management
- Event creation and scheduling
- Student event registration
- Attendance tracking
- Event dashboard and search
- Notifications and reminders
- AI-powered event recommendations in later versions
- Analytics and reporting

## Planned Software Versions

- Version 1: Core Event Management System
- Version 2: Intelligent Automation and Analytics
- Future enhancements: native mobile app, advanced ML personalization, multi-campus support, LMS integration

---

# 2. Product Scope

## Included Functionality

The repository explicitly supports the following scope:

- User registration and login
- Role-based access for administrators, faculty, students, and department heads
- Event creation, scheduling, and dashboard display
- Event search and viewing
- Student registration for events
- Basic attendance tracking
- Participation history viewing
- Notifications and reminders
- Event recommendations in later versions
- Attendance and participation reporting

## Excluded Functionality

The repository does not define the following as part of the initial scope:

- A native mobile application
- Advanced machine-learning personalization beyond the planned recommendation module
- Multi-campus support
- LMS integration such as Canvas or Moodle

## Future Enhancements

The repository identifies the following future enhancements:

- Native mobile app
- Advanced ML personalization
- Multi-campus support
- LMS integration

---

# 3. Software Capabilities

## 3.1 Level-1 Capabilities

The repository supports the following major capabilities:

1. Manage Users and Roles
2. Manage Events
3. Manage Registrations
4. Track Attendance
5. Notify Users
6. Recommend Events
7. Generate Reports and Analytics

## 3.2 Level-2 Capabilities

### 1. Manage Users and Roles

1.1 Register User

1.2 Authenticate User

1.3 Manage User Roles

### 2. Manage Events

2.1 Create Event

2.2 Update Event

2.3 Search Events

2.4 View Event Dashboard

### 3. Manage Registrations

3.1 Register for Event

3.2 Approve Registration

3.3 View Participation History

### 4. Track Attendance

4.1 Record Attendance

4.2 Verify Attendance with QR

### 5. Notify Users

5.1 Send Event Notifications

5.2 Send Reminders

### 6. Recommend Events

6.1 Generate Recommendations

### 7. Generate Reports and Analytics

7.1 Generate Attendance Reports

7.2 Analyze Participation Trends

7.3 View Analytics Dashboard

---

# 4. Undesirable Events

| UE ID | Level-2 Capability | Undesirable Event |
|-------|--------------------|-------------------|
| UE-1.1-01 | Register User | Duplicate or conflicting user account is created |
| UE-1.2-01 | Authenticate User | Unauthorized user gains access to the system |
| UE-1.3-01 | Manage User Roles | A user is assigned an incorrect role |
| UE-2.1-01 | Create Event | An event is created with incomplete or inconsistent information |
| UE-2.2-01 | Update Event | An event update is not applied consistently across the system |
| UE-2.3-01 | Search Events | Users cannot find relevant events through the search experience |
| UE-2.4-01 | View Event Dashboard | The dashboard displays outdated or inaccurate event information |
| UE-3.1-01 | Register for Event | A student registers beyond the event capacity |
| UE-3.2-01 | Approve Registration | Registration approval is delayed or applied inconsistently |
| UE-3.3-01 | View Participation History | A student’s participation history is inaccurate or missing |
| UE-4.1-01 | Record Attendance | Attendance is recorded incorrectly for an event |
| UE-4.2-01 | Verify Attendance with QR | QR-based attendance verification is bypassed or misread |
| UE-5.1-01 | Send Event Notifications | An event notification is not delivered to the intended user |
| UE-5.2-01 | Send Reminders | A reminder is sent too late or not at all |
| UE-6.1-01 | Generate Recommendations | Recommendations are irrelevant or inaccurate for a student |
| UE-7.1-01 | Generate Attendance Reports | An attendance report contains incorrect or incomplete data |
| UE-7.2-01 | Analyze Participation Trends | Trend analysis is misleading because underlying data is incomplete |
| UE-7.3-01 | View Analytics Dashboard | The analytics dashboard is unavailable or not updated |

---

# 5. Risk Analysis

| UE ID | Risk Statement | Likelihood | Impact | Risk Score |
|-------|----------------|------------|--------|------------|
| UE-3.1-01 | Over-capacity registration may create inaccurate attendance and event management outcomes | 3 | 4 | 12 |
| UE-4.1-01 | Incorrect attendance recording may undermine trust in the system and reporting | 3 | 4 | 12 |
| UE-4.2-01 | QR verification failure may allow fraudulent or inaccurate attendance results | 3 | 4 | 12 |
| UE-6.1-01 | Poor recommendations may reduce student engagement and make the smart feature ineffective | 4 | 3 | 12 |
| UE-7.1-01 | Incorrect reporting may lead to poor decisions by administrators or department heads | 3 | 4 | 12 |
| UE-1.2-01 | Unauthorized access may expose sensitive information and compromise system integrity | 2 | 5 | 10 |
| UE-1.3-01 | Incorrect role assignment may grant or deny access inappropriately | 2 | 4 | 8 |
| UE-2.1-01 | Incomplete event data may reduce the usefulness of the event management workflow | 3 | 3 | 9 |
| UE-2.4-01 | Inaccurate dashboard content may mislead users about current scheduling information | 3 | 3 | 9 |
| UE-3.3-01 | Inaccurate participation history may reduce trust in student engagement records | 3 | 3 | 9 |
| UE-5.1-01 | Notification failure may reduce communication effectiveness and participation | 3 | 3 | 9 |
| UE-5.2-01 | Reminder failure may cause missed registration deadlines or low attendance | 3 | 3 | 9 |
| UE-7.2-01 | Misleading trend analysis may cause incorrect institutional decisions | 3 | 3 | 9 |
| UE-1.1-01 | Duplicate accounts may create confusion and inconsistent user records | 2 | 3 | 6 |
| UE-2.2-01 | Inconsistent event updates may leave users with conflicting event information | 2 | 3 | 6 |
| UE-2.3-01 | Search failure may prevent users from finding relevant events | 3 | 2 | 6 |
| UE-3.2-01 | Inconsistent approvals may create unfair or delayed registration outcomes | 2 | 3 | 6 |
| UE-7.3-01 | Dashboard unavailability may limit reporting and analysis for stakeholders | 2 | 3 | 6 |

---

# 6. Risk Prioritization

| Priority | UE ID | Risk Score |
|----------|-------|------------|
| 1 | UE-3.1-01 | 12 |
| 2 | UE-4.1-01 | 12 |
| 3 | UE-4.2-01 | 12 |
| 4 | UE-6.1-01 | 12 |
| 5 | UE-7.1-01 | 12 |
| 6 | UE-1.2-01 | 10 |
| 7 | UE-1.3-01 | 8 |
| 8 | UE-2.1-01 | 9 |
| 9 | UE-2.4-01 | 9 |
| 10 | UE-3.3-01 | 9 |
| 11 | UE-5.1-01 | 9 |
| 12 | UE-5.2-01 | 9 |
| 13 | UE-7.2-01 | 9 |
| 14 | UE-1.1-01 | 6 |
| 15 | UE-2.2-01 | 6 |
| 16 | UE-2.3-01 | 6 |
| 17 | UE-3.2-01 | 6 |
| 18 | UE-7.3-01 | 6 |

---

# 7. Risk Mitigation

| UE ID | Risk Mitigation | Classification |
|-------|-----------------|----------------|
| UE-3.1-01 | Enforce capacity checks before registration and display remaining capacity clearly | Pure Software |
| UE-4.1-01 | Validate attendance entries, maintain audit-friendly records, and test attendance workflows | Pure Software |
| UE-4.2-01 | Validate QR-based attendance flow with fallback handling and device checks | Hybrid (Software + Hardware) |
| UE-6.1-01 | Start with simple recommendation logic and test recommendation quality using available participation data | Pure Software |
| UE-7.1-01 | Cross-check report inputs against stored attendance and registration data | Pure Software |
| UE-1.2-01 | Enforce role-based access controls and authentication checks for all sensitive actions | Pure Software |
| UE-1.3-01 | Restrict role updates to authorized administrators and validate role changes before application | Pure Software |
| UE-2.1-01 | Require required event fields before creation and validate field completeness | Pure Software |
| UE-2.4-01 | Refresh dashboard data from the central data store and validate event state before display | Pure Software |
| UE-3.3-01 | Persist participation history from registration and attendance workflows and test for consistency | Pure Software |
| UE-5.1-01 | Use reliable notification service integration and log delivery attempts for monitoring | Pure Software |
| UE-5.2-01 | Trigger reminder workflows from event and deadline data and monitor delivery outcomes | Pure Software |
| UE-7.2-01 | Validate trend analysis inputs and ensure datasets are complete before reporting | Pure Software |
| UE-1.1-01 | Prevent duplicate registration by checking existing accounts before creating a new user | Pure Software |
| UE-2.2-01 | Apply event updates through centralized workflow logic and verify state changes | Pure Software |
| UE-2.3-01 | Ensure search indexes and query logic cover event titles, categories, and upcoming schedules | Pure Software |
| UE-3.2-01 | Apply approval actions through a defined workflow and track approval state consistently | Pure Software |
| UE-7.3-01 | Maintain dashboard availability through testing, monitoring, and fail-safe display logic | Pure Software |

---

# 8. Functional Requirements

| Requirement ID | Level-2 Capability | Functional Requirement |
|----------------|--------------------|------------------------|
| FR-1.1.1 | Register User | The system shall register a new user with a role within the system. |
| FR-1.2.1 | Authenticate User | The authentication service shall authenticate a registered user within two seconds under normal operating conditions. |
| FR-1.3.1 | Manage User Roles | The role management module shall assign or update a user’s role within the system. |
| FR-2.1.1 | Create Event | The event management service shall create an event with a title, venue, time, category, capacity, and description. |
| FR-2.2.1 | Update Event | The event management service shall update an existing event within the system. |
| FR-2.3.1 | Search Events | The dashboard shall search and display events based on relevant filters and user input. |
| FR-2.4.1 | View Event Dashboard | The dashboard shall display upcoming events for authorized users. |
| FR-3.1.1 | Register for Event | The registration service shall allow a student to register for an event within the event capacity. |
| FR-3.2.1 | Approve Registration | The registration service shall approve or deny registrations for an event. |
| FR-3.3.1 | View Participation History | The system shall display a student’s participation history. |
| FR-4.1.1 | Record Attendance | The attendance service shall record attendance for an event. |
| FR-4.2.1 | Verify Attendance with QR | The attendance service shall verify attendance using QR-based validation. |
| FR-5.1.1 | Send Event Notifications | The notification service shall send event notifications to users through supported communication channels. |
| FR-5.2.1 | Send Reminders | The notification service shall send reminders before an event or registration deadline. |
| FR-6.1.1 | Generate Recommendations | The recommendation engine shall generate event recommendations based on available user and participation data. |
| FR-7.1.1 | Generate Attendance Reports | The reporting service shall generate attendance reports for an event or set of events. |
| FR-7.2.1 | Analyze Participation Trends | The analytics service shall analyze participation trends for reporting purposes. |
| FR-7.3.1 | View Analytics Dashboard | The analytics service shall present attendance and participation insights through a dashboard. |

---

# 9. Quality Requirements

The repository does not define quantitative quality targets. The following quality requirements are therefore proposed for implementation planning and validation:

- Security: The system shall enforce role-based access so that administrators, faculty coordinators, students, and department heads can only access the functions appropriate to their role.
- Reliability: The system shall persist event, registration, attendance, and report data so that normal operations do not lose records.
- Availability: The system shall remain available for core workflows such as login, event viewing, registration, attendance recording, and reporting during normal operating hours.
- Maintainability: The system shall use modular services and document major changes in the repository so that future updates are manageable.
- Scalability: The system architecture shall support the addition of new features from Version 1 to Version 2 and beyond without replacing the core event and attendance workflows.
- Usability: The dashboard shall provide users with clear access to events, registration actions, attendance information, and reporting features.
- Interoperability: The system shall integrate with external services for notifications, AI recommendations, and QR-based attendance support.
- Testability: The system shall expose core workflows for verification through functional testing.
- AI Explainability and AI Safety: These are planned for Version 2 but are not fully specified in the repository and remain To Be Completed.

---

# 10. Performance Requirements

The repository does not define explicit numerical performance targets. The following proposed performance requirements should be validated during implementation:

- Authentication and basic dashboard operations shall complete within two seconds for standard user requests.
- Event search and event listing shall return results within two seconds for a typical dataset.
- Attendance recording and QR verification shall complete within two seconds after the user submits the relevant action.
- Notification dispatch shall be initiated within one minute of the triggering event or reminder condition.
- The system shall support the planned Version 1 and Version 2 workflows without requiring a redesign of the core services.

---

# 11. Assumptions

- The system will be developed incrementally through Version 1 and Version 2.
- The system will provide a web-based portal for students and administrators.
- Users will be assigned roles such as administrator, faculty coordinator, student, and department head.
- Event data will be stored and managed centrally.
- Notification delivery may rely on external email or SMS APIs.
- Recommendation functionality will be introduced in later versions and may use third-party AI or machine learning services.
- Attendance verification will use QR-based support in later planned functionality.
- The repository will continue to be used for version control and documentation.

---

# 12. Constraints

- The repository does not define a specific implementation language, framework, or database engine beyond the use of a relational database concept in the system architecture.
- The repository does not define a specific operating system or deployment environment.
- The project scope is constrained by semester-based development expectations.
- The system depends on external services for notifications and AI recommendations.
- The repository does not define hardware requirements beyond the general concept of QR-based attendance support.
- The repository identifies future enhancements that are not part of the initial scope.

---

# 13. External Interfaces

## User Interfaces

- Student and administrator web portal
- Event dashboard and search interface
- Registration and participation history views
- Analytics and reporting dashboard
- Future mobile application interface

## Hardware Interfaces

- QR scanning or camera-enabled device support for attendance verification

## Software Interfaces

- Authentication and role management service
- Event management service
- Registration and attendance service
- Recommendation engine
- Notification service
- Analytics and reporting service
- Relational database for users, events, and attendance
- Cache or session store
- QR code service

## Communication Interfaces

- Communication between the web portal and backend services
- Communication between backend services and the relational data store
- Communication with external notification services such as email or SMS APIs
- Communication with third-party AI or machine learning services for recommendations

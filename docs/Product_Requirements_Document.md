# Product Requirements Document (PRD)

## 1. Scope and evidence basis

This document is based on the repository evidence in README.md, backend/, api/, config/, ai_recommendation/, frontend/, database/, docs/, test/, .github/workflows/, and the authoritative risk register supplied in the project brief. Where the repository does not provide evidence of a capability, requirement, or control, the status is marked as "To Be Completed."

---

## 2. Level-1 and Level-2 capabilities

### 1. Authenticate and authorize users

#### 1.1 Register a user
- Status: Implemented in current code.
- Evidence: backend/routes/auth.py defines POST /register and echoes the submitted user data.

#### 1.2 Authenticate credentials
- Status: Implemented in current code.
- Evidence: backend/routes/auth.py defines POST /login and checks hardcoded admin credentials.

#### 1.3 Enforce role-based access control
- Status: Planned / To Be Completed.
- Evidence: README.md claims role-based access control, but the repository does not show a real role enforcement mechanism beyond a role field in payloads.

#### 1.4 Audit login and access events
- Status: Planned / To Be Completed.
- Evidence: no audit logging or event trail is implemented in the repository.

### 2. Manage event lifecycle

#### 2.1 Create an event
- Status: Implemented in current code.
- Evidence: backend/routes/events.py defines POST /events and appends to an in-memory list.

#### 2.2 View events
- Status: Implemented in current code.
- Evidence: backend/routes/events.py defines GET /events.

#### 2.3 Update an event
- Status: Planned / To Be Completed.
- Evidence: README.md advertises update events, but no route is registered in the running Flask app.

#### 2.4 Delete an event
- Status: Planned / To Be Completed.
- Evidence: README.md advertises delete events, but no working route is registered in the running Flask app.

### 3. Manage registrations and capacity

#### 3.1 Register a student to an event
- Status: Planned / To Be Completed.
- Evidence: frontend and README describe event registration, but the current event registration flow is not implemented as a real capacity-aware registration feature.

#### 3.2 Validate event capacity
- Status: Planned / To Be Completed.
- Evidence: README.md and the risk register reference capacity constraints, but no capacity validation logic is present in the current source.

#### 3.3 Notify users when an event is full or waitlisted
- Status: Planned / To Be Completed.
- Evidence: no waitlist or overbooking logic is present in the repository.

### 4. Record attendance

#### 4.1 Mark attendance for a student
- Status: Implemented in current code.
- Evidence: backend/routes/attendance.py defines POST /attendance and echoes the submitted data.

#### 4.2 View attendance reports
- Status: Implemented in current code.
- Evidence: backend/routes/attendance.py defines GET /attendance and returns a static list sample.

#### 4.3 Validate QR-based attendance
- Status: Planned / To Be Completed.
- Evidence: README.md claims QR code attendance verification, but no QR route or QR validation logic is present in backend/, api/, or frontend/.

### 5. Notify users

#### 5.1 Send email or SMS notifications
- Status: Partial / stubbed implementation.
- Evidence: backend/routes/notifications.py returns a canned success response for POST /notify, and backend/email_service.py exists but is not actually called from the route.

#### 5.2 Retry or log failed delivery
- Status: Planned / To Be Completed.
- Evidence: no retry, log, or delivery-status mechanism is implemented.

### 6. Generate recommendations

#### 6.1 Train the recommendation model
- Status: Implemented in current code.
- Evidence: ai_recommendation/train_model.py and model training scripts exist and can generate model.pkl.

#### 6.2 Recommend events to a student based on interests
- Status: Implemented in current code.
- Evidence: ai_recommendation/recommendation_engine.py and corresponding tests exercise interest-based recommendations.

### 7. Maintain data and system availability

#### 7.1 Persist application data in a database
- Status: Partial / dependent on local environment setup.
- Evidence: database/ SQL files and backend/database.py exist, but the repository’s setup instructions and actual test execution show database schema and configuration issues.

#### 7.2 Recover from database or service interruption
- Status: Planned / To Be Completed.
- Evidence: no backup, replication, failover, or recovery process is implemented in the repository.

#### 7.3 Monitor service health and application state
- Status: Planned / To Be Completed.
- Evidence: no health check endpoints, monitoring, or alerting logic are present.

---

## 3. Undesirable events

The following undesirable events are derived from the authoritative risk register and traced to the corresponding Level-2 capability.

| Risk ID | Undesirable Event | Level-2 capability |
| --- | --- | --- |
| R4 | Unauthorized access | 1.2 Authenticate credentials / 1.3 Enforce role-based access control |
| R5 | Registration exceeds capacity | 3.2 Validate event capacity |
| R8 | Database unavailable | 7.1 Persist application data in a database |
| R6 | Notification failure | 5.1 Send email or SMS notifications |
| R7 | QR scan failure | 4.3 Validate QR-based attendance |

Additional undesirable events identified from repository evidence:

| ID | Undesirable Event | Level-2 capability |
| --- | --- | --- |
| U1 | Password disclosure in API responses | 1.1 Register a user |
| U2 | Unhandled malformed input causes 500 errors | 1.2 Authenticate credentials / 5.1 Send email or SMS notifications |
| U3 | Schema setup does not reliably produce the expected tables | 7.1 Persist application data in a database |

---

## 4. Risks

These risks are reproduced from the authoritative register exactly, ordered highest to lowest by Risk Score.

| Risk ID | Undesirable Event | Likelihood | Consequence | Risk Score | Likelihood Justification | Consequence Justification | Mitigation | Q1 (Desired) | Q2 (Preventative) | Q3 (Responsive/Recovery) | Mitigation Type | Classification Justification |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| R4 | Unauthorized access | 4 | 5 | 20 | Weak credentials | Data breach | MFA, RBAC, encryption | Authenticate authorized users | Reject invalid access | Lock account & notify | Pure Software | MFA/RBAC/encryption are software-enforced controls without a hardware prerequisite. |
| R5 | Registration exceeds capacity | 3 | 4 | 12 | Popular events | Overbooking | Capacity validation | Register if seats available | Block full events | Waitlist | Pure Software | Capacity validation and waitlist logic are code-driven workflow controls, not hardware dependency. |
| R8 | Database unavailable | 2 | 5 | 10 | Server outage | Service interruption | Replication/failover | Keep DB available | Prevent corruption | Failover | Hybrid | Replication/failover depends on infrastructure and software together, not hardware alone. |
| R6 | Notification failure | 3 | 3 | 9 | Service outage | Missed alerts | Retry & backup | Send notifications | Don't mark failed delivery | Retry/log | Pure Software | Retry logic, logging, and backup delivery are software-controlled behaviors. |
| R7 | QR scan failure | 2 | 4 | 8 | Damaged QR | Wrong attendance | Manual override | Scan QR | Reject invalid QR | Manual attendance | Hybrid | Manual override requires a human process step in addition to software validation. |

---

## 5. Functional requirements (ABC format)

The following requirements use the Actor-Behavior-Constraint format. IDs FR4.1, FR4.2, FR5.1, FR6.1, FR7.1, and FR8.1 are preserved exactly as required from the authoritative risk register.

### Authentication and access control

- FR4.1: The user shall authenticate with authorized credentials within the system’s security constraints to access the protected campus system features.
- FR4.2: The user shall be limited by role-based access control within the security policy to prevent unauthorized actions.
- FR1.1: The student or administrator shall register with a valid user payload within the required fields and role information to create an account.
- FR1.2: The student or administrator shall log in with valid credentials within the authentication rules to access the application.

### Event registration and capacity management

- FR5.1: The user shall register for an event only when capacity is available within the event’s seat limit to prevent overbooking.
- FR2.1: The administrator shall create an event with valid event details within the system’s required data model.
- FR2.2: The user shall view the list of available events within the application to select an event.
- FR2.3: The administrator shall update an event within the defined event model when the event record changes.
- FR2.4: The administrator shall delete an event within the allowed lifecycle rules when the event is removed.

### Attendance and QR tracking

- FR7.1: The user shall scan a valid QR code within the attendance verification process to record attendance.
- FR4.3: The system shall mark attendance for a student within the valid attendance record constraints to record participation.
- FR4.4: The user shall retrieve an attendance report within the system’s access policy to review participation history.

### Notifications and service availability

- FR6.1: The system shall send a notification to the specified recipient within the configured delivery pipeline to communicate event or status information.
- FR6.2: The system shall retry or log failed notification delivery within the reliability requirements to avoid silent loss of alerts.

### Data persistence and recovery

- FR8.1: The system shall maintain data availability within the configured database architecture to avoid service interruption.
- FR8.2: The system shall recover or restore service after a database failure within the recovery process requirements to resume operation.
- FR8.3: The system shall validate database setup and schema integrity within the repository’s documented process to ensure required data tables exist.

### Recommendation capability

- FR9.1: The AI engine shall train a recommendation model from the provided dataset within the project’s training process.
- FR9.2: The system shall generate an event recommendation for a student based on their interests within the model’s supported inputs.

---

## 6. Quality and performance requirements

The following quality and performance requirements are measurable only. Unsupported values are marked as "To Be Completed."

| Requirement ID | Requirement | Threshold / Measure |
| --- | --- | --- |
| QP-01 | Authentication response time for valid logins | To Be Completed. |
| QP-02 | Event registration must reject attempts that exceed capacity | To Be Completed. |
| QP-03 | Notification delivery status must be retriable and auditable | To Be Completed. |
| QP-04 | QR attendance validation must reject invalid scans before recording attendance | To Be Completed. |
| QP-05 | Database recovery process must restore service after outage | To Be Completed. |
| QP-06 | Model training must complete successfully with the repository dataset | To Be Completed. |
| QP-07 | The Python AST validation pass must succeed across all repository Python source files | To Be Completed. |

---

## 7. Revision history

| Date | Version | Author | Summary |
| --- | --- | --- | --- |
| 2026-08-13 | v0.1 | Senior SQA / Product Analyst | Initial PRD generated from repository evidence and the authoritative risk register; includes Level-1/Level-2 capabilities, risks, requirements, and quality constraints. |

---

## 8. Implementation status summary

| Capability | Current status |
| --- | --- |
| User authentication | Partially implemented |
| Role-based access control | Planned / To Be Completed |
| Event creation/viewing | Implemented |
| Event update/delete | Planned / To Be Completed |
| Event capacity control | Planned / To Be Completed |
| Attendance recording/reporting | Partially implemented |
| QR-based attendance | Planned / To Be Completed |
| Notification dispatch | Stubbed / partial |
| Recommendation model training and inference | Implemented |
| Database persistence and recovery | Partial / To Be Completed |

This PRD is intentionally conservative. It reflects only the repository evidence available at the time of authoring and the authoritative risk register supplied for this project.

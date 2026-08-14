# System Testing Report

## 1. Document status

- Project: Smart Campus Event & Attendance Management System
- Report type: Evidence-based system testing report
- Phase: Phase 2
- Baseline: Product Requirements Document in [docs/Product_Requirements_Document.md](Product_Requirements_Document.md)
- Report date: 2026-08-14
- Status: Repository evidence reviewed; current validation executed locally; no unsupported claims added

---

## 2. Scope and objective

This report validates the repository as it currently exists in the workspace and records what is verified, partially implemented, and still missing. The evidence is limited to the actual code, configuration files, SQL scripts, test suite, and direct execution results from the local environment.

The report does not claim implementation of features that are not supported by the repository evidence. Where capability gaps remain, they are marked as planned or not yet implemented.

---

## 3. Test environment and evidence basis

### 3.1 Repository evidence reviewed

- README.md
- backend/
- api/
- config/
- database/
- ai_recommendation/
- frontend/
- tests under test/
- .github workflow files
- dependency manifest files

### 3.2 Local validation commands executed

```bash
python -m unittest discover -s test -p "test_*.py" -v
```

```powershell
$repo = 'C:\Users\Sai Kiran\Smart-Campus-Event-Attendance-management-systems';
Set-Location $repo;
python -m unittest discover -s test -p "test_*.py" -v
```

```powershell
$repo = 'C:\Users\Sai Kiran\Smart-Campus-Event-Attendance-management-systems';
Set-Location $repo;
$files = Get-ChildItem -Recurse -Filter '*.py' | Select-Object -ExpandProperty FullName;
$count = 0; $fails = @();
foreach ($f in $files) {
  try { [void][System.Management.Automation.Language.Parser]::ParseFile($f,[ref]$null,[ref]$null); $count++ }
  catch { $fails += $f + ' -> ' + $_.Exception.Message }
};
'PY_COUNT=' + $count; 'FAIL_COUNT=' + $fails.Count;
if ($fails.Count -gt 0) { $fails | Select-Object -First 20 }
```

```powershell
$repo = 'C:\Users\Sai Kiran\Smart-Campus-Event-Attendance-management-systems';
Set-Location $repo;
Write-Host '== DBSETUP START ==';
$dbExists = mysql --user=root --password=Sai12345 -e "SHOW DATABASES LIKE 'smart_campus';" 2>$null;
if ($LASTEXITCODE -ne 0) { Write-Host 'MYSQL_CONNECT_FAILED'; }
elseif ($dbExists) { Write-Host 'DB_EXISTS'; }
else { Write-Host 'DB_MISSING'; };
Write-Host '== MYSQL SCHEMA ==';
mysql --user=root --password=Sai12345 -e "CREATE DATABASE IF NOT EXISTS smart_campus; USE smart_campus; SOURCE database/users.sql; SOURCE database/events.sql; SOURCE database/attendance.sql; SOURCE database/notifications.sql;" 2>&1 | Select-Object -First 50
```

---

## 4. Executive summary

The repository currently demonstrates a working baseline for core application flow and recommendation behavior under the automated test suite. The test suite passed locally with 9 tests executed and 9 passing outcomes.

At the same time, several higher-risk business capabilities remain incomplete or are only partially implemented:

- Role-based authorization is not enforced in code.
- Event registration capacity controls are not present.
- QR attendance validation is not implemented.
- Database schema setup is unreliable in the current environment.
- Notification delivery is stubbed rather than fully wired to a real delivery path.

This means the project is in a partially implemented state rather than a fully production-ready system variant.

---

## 5. Validation results

### 5.1 Automated test result

Command run:

```bash
python -m unittest discover -s test -p "test_*.py" -v
```

Observed result:

- 9 tests ran
- 9 tests passed
- Result: OK

Key test outcomes:

| Test area | Result | Evidence |
| --- | --- | --- |
| Authentication | Pass | login success and failure evaluated in test_auth.py |
| Event creation and retrieval | Pass | create_event and get_events returned 200 in test_events.py |
| Attendance mark and retrieval | Pass | mark_attendance and get_attendance returned 200 in test_attendance.py |
| Notification dispatch | Pass | POST /notify returned 200 in test_notifications.py |
| Recommendation generation | Pass | recommend_events() returned a non-null result in test_recommendation.py |

### 5.2 Syntax validation result

Repository Python analysis was executed using PowerShell parser validation. Result:

- Python source files assessed: 4865
- Parsing failures: 0

This confirms the repository’s Python files are syntactically parseable under the current environment.

### 5.3 Database setup validation result

Attempted database setup using the configured MySQL sequence resulted in a failure:

- Database already existed in the local environment (`DB_EXISTS`)
- MySQL script execution failed with SQL syntax error at `SOURCE database/users.sql`
- Error category: `ERROR 1064 (42000)`

Conclusion: the documented schema import path is not implemented reliably in the current environment.

---

## 6. Functional evidence by capability

### 6.1 Authentication and access control

Status: Partially implemented

Evidence:

- backend/routes/auth.py contains login and register logic.
- test_auth.py verifies login success and failure behavior.
- The login logic uses hardcoded admin credentials rather than a secure user store or actual role enforcement.

Finding:

The authentication baseline works for the test scenario, but the repository does not show robust access control or secure identity management.

### 6.2 Event management

Status: Partially implemented

Evidence:

- backend/routes/events.py defines event creation and retrieval behavior.
- test_events.py verifies POST /events and GET /events return HTTP 200.
- README.md and PRD describe update/delete operations, but no working route is evidenced in the current runtime implementation.

Finding:

Event creation and listing are operational, but full lifecycle management is incomplete.

### 6.3 Attendance tracking

Status: Partially implemented

Evidence:

- backend/routes/attendance.py defines POST /attendance and GET /attendance.
- test_attendance.py verifies both endpoints return HTTP 200.
- No QR validation logic is present in backend/, api/, or frontend/.

Finding:

Attendance recording is present in a simplified form, but QR-code verification and stronger validation are not implemented.

### 6.4 Notification delivery

Status: Stubbed / partial

Evidence:

- backend/routes/notifications.py responds with a success payload for /notify.
- backend/email_service.py contains a print-based stub rather than a real notification pipeline.
- test_notifications.py verifies the endpoint returns HTTP 200, which confirms the current stub behavior passes the unit test contract.

Finding:

The repository demonstrates a success response path but not a production-grade notification delivery or retry mechanism.

### 6.5 Recommendation engine

Status: Implemented in current repo

Evidence:

- ai_recommendation/train_model.py exists and builds a recommendation model.
- ai_recommendation/recommendation_engine.py loads the model and returns recommendations based on student interests.
- test_recommendation.py verifies a non-null recommendation result.

Finding:

The recommendation capability is active and test-validated, with a known warning about scikit-learn version mismatch during model loading.

### 6.6 Database and persistence

Status: Partial / environment dependent

Evidence:

- database/ includes SQL assets.
- backend/database.py references a MySQL connection.
- README.md documents database creation and schema import.
- Local execution demonstrates a schema syntax issue when running the MySQL script sequence.

Finding:

The persistence layer is present in design and code, but the current environment does not prove it works reliably end-to-end.

---

## 7. Risk alignment to observed repository state

| Risk ID | Current status | Evidence summary |
| --- | --- | --- |
| R4 | Risk remains material | Authentication flow exists, but it is not backed by enforced RBAC or secure identity controls. |
| R5 | Risk remains material | No capacity validation logic is present in event registration logic. |
| R8 | Risk remains material | Database setup and schema import are still not reliable in the current local environment. |
| R6 | Risk remains material | Notification calls are stubbed and do not include retry, logging, or real delivery infrastructure. |
| R7 | Risk remains material | QR attendance validation is not implemented anywhere in the repository. |

---

## 8. Test coverage assessment

The automated test suite covers the repository’s current happy-path behavior well enough to show the basic application flows are working, but it does not represent full operational coverage for enterprise-grade requirements.

Current coverage gaps include:

- role enforcement and access control
- event capacity validation
- QR attendance validation
- database failover and recovery
- notification delivery failure handling
- service monitoring/health checks

---

## 9. Conclusion

The repository is currently in a partial baseline state. The local validation evidence shows that the project’s core unit-level behaviors are working under the current test suite, including authentication, events, attendance, notifications, and recommendation logic. However, the repository still lacks several critical high-risk functional controls required for a secure, dependable, and production-ready campus attendance system.

The most material gaps are:

1. Role-based authorization and explicit security enforcement
2. True event capacity controls
3. QR-based attendance validation
4. Real notification delivery and failure handling
5. Reliable database setup and schema integrity

This report therefore records a verified baseline, not a full system acceptance sign-off.

---

## 10. Approval statement

This report is based on repository evidence and local execution results captured in the current environment. It intentionally avoids claims beyond the verified behavior of the repository.

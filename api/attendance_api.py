from flask import Blueprint, request, jsonify

attendance_api = Blueprint("attendance_api", **name**)

attendance_records = []

@attendance_api.route("/api/attendance", methods=["POST"])
def mark_attendance():

```
data = request.get_json()

attendance = {
    "student_id": data["student_id"],
    "event_id": data["event_id"],
    "status": data["status"]
}

attendance_records.append(attendance)

return jsonify({
    "message": "Attendance recorded",
    "attendance": attendance
})
```

@attendance_api.route("/api/attendance", methods=["GET"])
def get_attendance():

```
return jsonify(attendance_records)
```

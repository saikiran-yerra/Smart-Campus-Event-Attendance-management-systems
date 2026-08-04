from flask import Blueprint, request, jsonify


attendance_bp = Blueprint("attendance", __name__)


@attendance_bp.route("/attendance", methods=["POST"])
def add_attendance():

    data = request.json

    return jsonify({
        "message": "Attendance recorded successfully",
        "attendance": data
    })


@attendance_bp.route("/attendance", methods=["GET"])
def get_attendance():

    return jsonify([
        {
            "student_id": 1,
            "event_id": 1,
            "status": "Present"
        },
        {
            "student_id": 2,
            "event_id": 1,
            "status": "Absent"
        }
    ])
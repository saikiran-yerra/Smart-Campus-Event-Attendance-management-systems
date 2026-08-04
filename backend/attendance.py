from flask import Blueprint, request, jsonify

attendance_bp = Blueprint("attendance", __name__)


@attendance_bp.route("/attendance", methods=["POST"])
def add_attendance():

    data = request.json

    return jsonify({
        "message": "Attendance recorded successfully",
        "attendance": data
    })
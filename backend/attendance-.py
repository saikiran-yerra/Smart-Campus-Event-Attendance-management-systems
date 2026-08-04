from flask import Blueprint
from flask import jsonify
from flask import request

attendance_bp = Blueprint("attendance", __name__)

attendance_records = []


@attendance_bp.route("/attendance", methods=["POST"])
def mark_attendance():

    data = request.json

    attendance_records.append(data)

    return jsonify({

        "message": "Attendance marked",

        "data": data

    })


@attendance_bp.route("/attendance", methods=["GET"])
def get_attendance():

    return jsonify(attendance_records)
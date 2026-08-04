from flask import Blueprint
from flask import jsonify
from flask import request

events_bp = Blueprint("events", __name__)

events = []


@events_bp.route("/events", methods=["GET"])
def get_events():

    return jsonify(events)


@events_bp.route("/events", methods=["POST"])
def create_event():

    data = request.json

    events.append(data)

    return jsonify({

        "message": "Event created successfully",

        "event": data

    })
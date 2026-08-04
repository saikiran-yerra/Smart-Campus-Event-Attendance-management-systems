from flask import Blueprint
from flask import jsonify
from flask import request

notification_bp = Blueprint("notifications", __name__)


@notification_bp.route("/notify", methods=["POST"])
def send_notification():

    data = request.json

    return jsonify({

        "message": "Notification sent",

        "recipient": data["email"]

    })
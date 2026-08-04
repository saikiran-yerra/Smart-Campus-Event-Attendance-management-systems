from flask import Blueprint
from flask import request
from flask import jsonify

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    return jsonify({

        "message": "User registered successfully",

        "user": data

    })


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data["email"]

    password = data["password"]

    if email == "admin@gmail.com" and password == "admin":

        return jsonify({

            "message": "Login successful"

        })

    return jsonify({

        "message": "Invalid credentials"

    }), 401
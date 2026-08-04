from flask import Flask
from flask_cors import CORS

from backend.routes.auth import auth_bp
from backend.routes.events import events_bp
from backend.routes.attendance import attendance_bp
from backend.routes.notifications import notification_bp


app = Flask(__name__)

# Allow frontend (localhost:5500) to call Flask API
CORS(app)

app.config['SECRET_KEY'] = 'smartcampus123'


app.register_blueprint(auth_bp)
app.register_blueprint(events_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(notification_bp)


@app.route("/")
def home():
    return {
        "message": "Smart Campus Event & Attendance Management System"
    }


if __name__ == "__main__":
    app.run(debug=True)
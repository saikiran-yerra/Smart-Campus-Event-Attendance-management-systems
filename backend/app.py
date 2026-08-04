from flask import Flask
from routes.auth import auth_bp
from routes.events import events_bp
from routes.attendance import attendance_bp
from routes.notifications import notification_bp

app = Flask(__name__)

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
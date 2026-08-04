INSERT INTO users (full_name, email, password, role)

VALUES

('Admin User', '[admin@gmail.com](mailto:admin@gmail.com)', 'admin123', 'admin'),

('John Doe', '[john@gmail.com](mailto:john@gmail.com)', 'john123', 'student'),

('Jane Smith', '[jane@gmail.com](mailto:jane@gmail.com)', 'jane123', 'student');

INSERT INTO events (event_name, description, event_date, location, created_by)

VALUES

('Tech Fest 2026', 'Annual technology festival', '2026-08-10', 'Main Auditorium', 1),

('Hackathon', '24-hour coding competition', '2026-08-20', 'Computer Lab', 1);

INSERT INTO attendance (student_id, event_id, status)

VALUES

(2, 1, 'Present'),

(3, 1, 'Absent');

INSERT INTO notifications (user_id, message, status)

VALUES

(2, 'Welcome to Tech Fest 2026', 'Sent'),

(3, 'Hackathon registration is open', 'Pending');

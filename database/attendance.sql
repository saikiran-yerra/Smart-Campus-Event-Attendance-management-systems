CREATE TABLE attendance (


attendance_id INT AUTO_INCREMENT PRIMARY KEY,

student_id INT NOT NULL,

event_id INT NOT NULL,

status ENUM('Present', 'Absent') DEFAULT 'Absent',

attendance_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (student_id) REFERENCES users(user_id),

FOREIGN KEY (event_id) REFERENCES events(event_id)


);

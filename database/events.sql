CREATE TABLE events (

```
event_id INT AUTO_INCREMENT PRIMARY KEY,

event_name VARCHAR(200) NOT NULL,

description TEXT,

event_date DATE NOT NULL,

location VARCHAR(200),

created_by INT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (created_by) REFERENCES users(user_id)
```

);

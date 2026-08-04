CREATE TABLE notifications (

```
notification_id INT AUTO_INCREMENT PRIMARY KEY,

user_id INT NOT NULL,

message TEXT NOT NULL,

status ENUM('Sent', 'Pending') DEFAULT 'Pending',

sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (user_id) REFERENCES users(user_id)
```

);

import os

class Config:

```
SECRET_KEY = os.getenv(

    "SECRET_KEY",

    "smart-campus-secret"

)

DEBUG = False

TESTING = False
```

import unittest

from backend.utils.database import get_connection

class TestDatabase(unittest.TestCase):

```
def test_connection(self):

    connection = get_connection()

    self.assertIsNotNone(connection)

    connection.close()
```

if **name** == "**main**":

```
unittest.main()
```

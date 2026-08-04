import pandas as pd

def preprocess_data(file_name):

```
data = pd.read_csv(file_name)


data = data.dropna()


return data
```

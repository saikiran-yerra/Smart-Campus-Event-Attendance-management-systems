import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

import pickle

dataset = pd.read_csv("dataset.csv")

X = dataset[

```
[

    "technical_interest",

    "sports_interest",

    "cultural_interest"

]
```

]

y = dataset["recommended_event"]

X_train, X_test, y_train, y_test = train_test_split(

```
X,

y,

test_size=0.2,

random_state=42
```

)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

with open("model.pkl", "wb") as file:

```
pickle.dump(model, file)
```

print("Model trained successfully")

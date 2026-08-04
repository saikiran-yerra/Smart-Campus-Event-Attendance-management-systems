import pandas as pd
import pickle

with open("model.pkl", "rb") as file:
model = pickle.load(file)

def recommend_events(student_interests):

```
data = pd.DataFrame({

    "technical_interest": [
        student_interests["technical_interest"]
    ],

    "sports_interest": [
        student_interests["sports_interest"]
    ],

    "cultural_interest": [
        student_interests["cultural_interest"]
    ]

})

prediction = model.predict(data)

events = {

    0: "Hackathon",

    1: "Football Tournament",

    2: "Cultural Fest"

}

return events[prediction[0]]
```

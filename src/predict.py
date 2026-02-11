import joblib
import pandas as pd

model = joblib.load("model/mood_model.pkl")

sample = pd.DataFrame([{
    "energy": 0.88,
    "tempo": 145,
    "valence": 0.92,
    "danceability": 0.82,
    "loudness": -5
}])

prediction = model.predict(sample)

print("🎧 Recommended Mood:", prediction[0])

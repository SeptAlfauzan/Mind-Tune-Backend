from keras.models import load_model
import pandas as pd


def predict_track_genre(path: str, data: dict[str, any]):
    saved_model = load_model(path)
    data = pd.DataFrame(data)
    predicted = saved_model.predict(data)
    print(predicted)

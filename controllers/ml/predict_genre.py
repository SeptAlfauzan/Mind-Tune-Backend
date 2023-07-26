from keras.models import load_model
from helper.prediction import prediction_to_list, prediction_with_label
from models.track_genre_feature import TrackGenreFeature
import pandas as pd


def predict_track_genre(data: TrackGenreFeature):
    path = "./assets/ml/spotify_track_genre_rev.h5"
    saved_model = load_model(path)
    print(data)
    data_dict = {
        "danceability": [data.danceability],
        "energy": [data.energy],
        "key": [data.key],
        "loudness": [data.loudness],
        "speechiness": [data.speechiness],
        "acousticness": [data.acousticness],
        "instrumentalness": [data.instrumentalness],
        "liveness": [data.liveness],
        "valence": [data.valence],
        "tempo": [data.tempo],
        "duration_ms": [data.duration_ms],
    }
    df = pd.DataFrame(data_dict)
    predicted = saved_model.predict(df)
    list_pred = prediction_to_list(predicted)
    return prediction_with_label(list_pred)

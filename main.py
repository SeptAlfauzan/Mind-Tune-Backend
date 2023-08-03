from typing import Union, Annotated, Optional
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from helper.prediction import prediction_with_label
from models.track_genre_feature import TrackGenreFeature, TracksGenreFeature

# from models.track-genre-feature import TrackGenreFeature
from controllers.ml.predict_genre import predict_track_genre
from models.audio_features import AudioFeaturesModel
from models.top_track import TopTrackModel
from pydantic import BaseModel

import requests

app = FastAPI()
get_bearer_token = HTTPBearer(auto_error=False)


class DataObject:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/top/tracks/")
async def read_item(
    authorization: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
):
    audio_feature_url = "https://api.spotify.com/v1/audio-features/{}"
    top_tracks_url = (
        "https://api.spotify.com/v1/me/top/tracks?limit=20&time_range=short_term"
    )

    header = {
        "Authorization": "{} {}".format(authorization.scheme, authorization.credentials)
    }

    response = requests.get(
        url=top_tracks_url,
        headers=header,
    )

    response_json = response.json()

    if "error" in response_json:
        raise HTTPException(
            status_code=response_json["error"]["status"],
            detail=response_json["error"],
        )

    topTracks = TopTrackModel.validate(response_json)

    for track in topTracks.items:
        response_audio_features = requests.get(
            url=audio_feature_url.format(track.id),
            headers=header,
        )
        track.audio_features = AudioFeaturesModel.validate(
            response_audio_features.json()
        )

    return topTracks


# @app.post("/genre/tracks")
# def post_prediction(features: TracksGenreFeature):
#     data = {
#         "danceability": [0.923],
#         "energy": [0.508],
#         "key": [1],
#         "loudness": [-8.668],
#         "speechiness": [0.0468],
#         "acousticness": [0.104],
#         "instrumentalness": [1.21],
#         "liveness": [0.126],
#         "valence": [0.168],
#         "tempo": [108.039],
#         "duration_ms": [10],
#     }
#     predict_track_genre(data)
#     return {data: predict_track_genre}


@app.post("/genre/track")
def post_prediction(feature: TrackGenreFeature):
    pred = predict_track_genre(feature)
    json_data = jsonable_encoder(pred)

    print(json_data)
    return {"data": json_data}

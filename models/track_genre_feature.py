from typing import List
from pydantic import BaseModel


class TrackGenreFeature(BaseModel):
    danceability: float
    energy: float
    key: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration_ms: float


class TracksGenreFeature(BaseModel):
    features: List[TrackGenreFeature]

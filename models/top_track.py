# generated by datamodel-codegen:
#   filename:  top-tracks.json
#   timestamp: 2023-07-18T15:19:53+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel

from models.audio_features import AudioFeaturesModel


class ExternalUrls(BaseModel):
    spotify: str


class Artist(BaseModel):
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str


class Image(BaseModel):
    height: int
    url: str
    width: int


class Album(BaseModel):
    album_type: str
    artists: List[Artist]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    total_tracks: int
    type: str
    uri: str


class Artist1(BaseModel):
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str


class ExternalIds(BaseModel):
    isrc: str


class Item(BaseModel):
    album: Album
    artists: List[Artist1]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrls
    href: str
    id: str
    is_local: bool
    name: str
    popularity: int
    preview_url: str | None
    track_number: int
    type: str
    uri: str
    audio_features: AudioFeaturesModel | None = None


class TopTrackModel(BaseModel):
    items: List[Item]
    total: int
    limit: int
    offset: int
    href: str
    next: str
    previous: None
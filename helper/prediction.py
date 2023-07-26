from typing import List


def prediction_to_list(data):
    return [item.tolist() for item in data]


def prediction_with_label(data: List[List[str]]):
    genre_labels = [
        "classical",
        "country",
        "edm",
        "folk",
        "gospel",
        "hip-hop",
        "jazz",
        "k-pop",
        "metal",
        "pop",
        "rock",
    ]

    return [
        {key: value for key, value in zip(genre_labels, val_pred)} for val_pred in data
    ]

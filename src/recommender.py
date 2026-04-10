from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    print(f"Loaded Songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> float:
    genre_score = 2.0 if song["genre"] == user_prefs["genre"] else 0.0
    mood_score = 1.0 if song["mood"] == user_prefs["mood"] else 0.0
    energy_score = 1.0 - abs(user_prefs["energy"] - song["energy"])
    return genre_score + mood_score + energy_score

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = [
        (
            song,
            score_song(user_prefs, song),
            f"Genre {'matched' if song['genre'] == user_prefs['genre'] else 'did not match'}, "
            f"mood {'matched' if song['mood'] == user_prefs['mood'] else 'did not match'}, "
            f"energy difference: {abs(user_prefs['energy'] - song['energy']):.2f}"
        )
        for song in songs
    ]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]

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
        """Store the catalog of songs for later scoring."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs for the given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a plain-English explanation of why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv and return a list of song dicts with numeric fields cast to float."""
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
    """Score a song 0.0–4.0 based on genre, mood, and energy similarity to user prefs."""
    genre_score = 2.0 if song["genre"] == user_prefs["genre"] else 0.0
    mood_score = 1.0 if song["mood"] == user_prefs["mood"] else 0.0
    energy_score = 1.0 - abs(user_prefs["energy"] - song["energy"])
    return genre_score + mood_score + energy_score

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song in the catalog and return the top k sorted by score descending."""
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

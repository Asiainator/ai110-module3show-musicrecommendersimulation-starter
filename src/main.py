"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


PROFILES = {
    # --- Standard profiles ---
    "Starter (Pop/Happy)": {
        "genre": "pop", "mood": "happy", "energy": 0.8
    },
    "High-Energy Pop": {
        "genre": "pop", "mood": "happy", "energy": 0.95
    },
    "Chill Lofi": {
        "genre": "lofi", "mood": "chill", "energy": 0.35
    },
    "Deep Intense Rock": {
        "genre": "rock", "mood": "intense", "energy": 0.90
    },

    # --- Edge cases ---
    # Minimum possible energy — should surface the quietest ambient tracks
    "Dead Quiet (energy=0.0)": {
        "genre": "ambient", "mood": "chill", "energy": 0.0
    },
    # Maximum possible energy — nothing in the catalog reaches 1.0
    "Full Blast (energy=1.0)": {
        "genre": "rock", "mood": "intense", "energy": 1.0
    },

    # --- Adversarial profiles ---
    # Genre and mood exist but never appear together in the catalog
    # expects 0 matches on both categoricals, ranked purely by energy
    "Genre+Mood Mismatch (jazz/intense)": {
        "genre": "jazz", "mood": "intense", "energy": 0.7
    },
    # Genre that does not exist in the catalog at all
    # score will be energy-only for every song (max 3.0 unreachable)
    "Unknown Genre (classical)": {
        "genre": "classical", "mood": "relaxed", "energy": 0.3
    },
}


def run_profile(name: str, prefs: dict, songs: list, k: int = 5) -> None:
    print(f"\n{'='*55}")
    print(f"Profile: {name}")
    print(f"Prefs:   genre={prefs['genre']}  mood={prefs['mood']}  energy={prefs['energy']}")
    print(f"{'='*55}")
    results = recommend_songs(prefs, songs, k=k)
    for song, score, explanation in results:
        print(f"  {song['title']:<25} Score: {score:.2f}  |  {explanation}")


def main() -> None:
    songs = load_songs("data/songs.csv")
    for name, prefs in PROFILES.items():
        run_profile(name, prefs, songs)


if __name__ == "__main__":
    main()

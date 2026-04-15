from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

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
    """Loads songs from a CSV file."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric fields to appropriate types
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    
    print(f"Loaded {len(songs)} songs.")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences."""
    score = 0.0
    reasons = []
    # Genre Match: +1.0 points (halved)
    if song['genre'].lower() == user_prefs['favorite_genre'].lower():
        score += 1.0
        reasons.append(f"Genre match: {song['genre']}")
    
    # Mood Match: +1.0 point
    if song['mood'].lower() == user_prefs['favorite_mood'].lower():
        score += 1.0
        reasons.append(f"Mood match: {song['mood']}")
    
    # Energy Similarity: 0.0–2.0 points (doubled)
    energy_diff = abs(float(song['energy']) - user_prefs['target_energy'])
    energy_score = 2.0 - 2 * energy_diff
    score += energy_score
    reasons.append(f"Energy similarity: {energy_score:.2f} (song: {song['energy']}, target: {user_prefs['target_energy']})")
    
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Returns top k song recommendations based on user preferences."""
    def score_with_explanation(song):
        """Helper: score a song and format reasons as single explanation string."""
        score, reasons = score_song(user_prefs, song)
        explanation = " | ".join(reasons)
        return (song, score, explanation)
    
    # Score all songs, sort by score descending, return top k
    return sorted(map(score_with_explanation, songs), key=lambda x: x[1], reverse=True)[:k]

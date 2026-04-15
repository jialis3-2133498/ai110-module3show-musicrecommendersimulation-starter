"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("../data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Display user profile
    print("\n" + "=" * 70)
    print("🎵 MUSIC RECOMMENDER SYSTEM")
    print("=" * 70)
    print(f"\n📊 Your Profile:")
    print(f"   Favorite Genre: {user_prefs['favorite_genre']}")
    print(f"   Favorite Mood: {user_prefs['favorite_mood']}")
    print(f"   Target Energy: {user_prefs['target_energy']}")
    
    # Display recommendations
    print(f"\n🎧 Top {len(recommendations)} Recommendations:")
    print("-" * 70)
    
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"\n{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f} points")
        print(f"   Reasons:")
        # Parse and display each reason on its own line
        reasons = explanation.split(" | ")
        for reason in reasons:
            print(f"     • {reason}")
    
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()

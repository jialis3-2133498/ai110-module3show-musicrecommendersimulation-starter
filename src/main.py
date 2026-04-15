"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# Define distinct user preference profiles
USER_PROFILES = [
    {
        "name": "High-Energy Pop",
        "favorite_genre": "pop",
        "favorite_mood": "intense",
        "target_energy": 0.9
    },
    {
        "name": "Chill Lofi",
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.4
    },
    {
        "name": "Deep Intense Rock",
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.9
    }
]


def main() -> None:
    songs = load_songs("../data/songs.csv") 

    # Display recommendations for each profile
    for profile in USER_PROFILES:
        user_prefs = profile
        recommendations = recommend_songs(user_prefs, songs, k=5)

        # Display user profile
        print("\n" + "=" * 70)
        print(f"🎵 MUSIC RECOMMENDER SYSTEM - {profile['name']}")
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

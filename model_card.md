# 🎧 Model Card: Music Recommender Simulation

## 1 . Model Name
VibeMatch Recommender

## 2. Goal / Task
Our system suggests music songs based on user preferences. It predicts which songs a person might like.

## 3. Data Used
We use 17 songs from a CSV file. Each song has genre, mood, energy level, and other features. The data covers pop, rock, lofi, and more genres. It misses some moods like sad or angry.

## 4. Algorithm Summary
We score songs by matching genre, mood, and energy. Genre match gives 1 point. Mood match gives 1 point. Energy match gives 0-2 points based on how close it is. Higher score means better match.

## 5. Observed Behavior / Biases
The system's energy similarity scoring uses a linear penalty that heavily disadvantages songs with energy levels differing by more than 0.5 from the user's target, effectively eliminating potentially good matches that align perfectly in genre and mood but have mismatched energy. This creates a significant bias against users seeking very low-energy (calm, meditative) or very high-energy (extreme, intense) music, as the dataset's energy range of 0.25-0.95 doesn't adequately cover these extremes, resulting in consistently lower recommendation quality for such users. Additionally, the rigid exact-matching for genre and mood prevents cross-pollination between related but non-identical categories, trapping users in filter bubbles where they're never exposed to adjacent musical styles that might suit their preferences.

## 6. Evaluation Process
We tested the recommender with three distinct user profiles: High-Energy Pop (pop genre, intense mood, 0.9 energy), Chill Lofi (lofi genre, chill mood, 0.4 energy), and Deep Intense Rock (rock genre, intense mood, 0.9 energy). For each profile, we examined the top 5 recommendations, looking for logical ranking based on genre/mood/energy matches and overall score coherence. We ran the system with both original weights (genre +2.0, mood +1.0, energy 0-1.0) and modified weights (genre +1.0, mood +1.0, energy 0-2.0) to test sensitivity. What surprised us was how dramatically rankings shifted with the weight change - songs with near-perfect energy matches jumped positions despite lacking genre alignment, revealing the system's vulnerability to scoring parameter tweaks and potential for unintended biases.

---

## 7. Intended Use and Non-Intended Use 

Use for fun music discovery in class. Don't use for real music apps or professional recommendations.

## 8. Ideas for Improvement

Add fuzzy matching for genres. Include acoustic preference in scoring. Add diversity to avoid same recommendations.

## 9. Personal Reflection

My biggest learning moment was seeing how tweaking the scoring weights completely changed the recommendations - it made me realize how sensitive these systems are to design choices, and why real-world recommenders need careful tuning. AI tools were super helpful for generating code, explaining concepts, but I had to double-check them, especially the logic and outputs to ensure correctness. Things about simple algorithms surprised me is that they capture basic preferences well, making results seem intuitive even without complexity. For future extended project, probably I can add more features like tempo, implement diversity, expand dataset.  

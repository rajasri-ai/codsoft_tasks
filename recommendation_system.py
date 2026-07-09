

movies = {
    "action": [
        "Avengers",
        "John Wick",
        "Mad Max: Fury Road"
    ],
    "comedy": [
        "3 Idiots",
        "Jumanji",
        "Free Guy"
    ],
    "drama": [
        "The Pursuit of Happyness",
        "Forrest Gump",
        "The Shawshank Redemption"
    ],
    "science fiction": [
        "Interstellar",
        "The Martian",
        "Inception"
    ]
}

print("===== Movie Recommendation System =====")
print("Available Genres:")
print("- Action")
print("- Comedy")
print("- Drama")
print("- Science Fiction")

genre = input("\nEnter your favorite genre: ").lower()

if genre in movies:
    print("\nRecommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("\nSorry! Genre not found.")
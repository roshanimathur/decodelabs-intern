# AI Recommendation Logic

movies = {
    "action": ["Avengers", "John Wick", "Mad Max"],
    "comedy": ["Mr. Bean", "The Mask", "Home Alone"],
    "drama": ["Titanic", "Forrest Gump", "The Pursuit of Happyness"]
}

print("Available categories:")
print("action, comedy, drama")

choice = input("Enter your favorite category: ").lower()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Sorry, category not found.")

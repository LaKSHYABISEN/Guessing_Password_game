import random 


easy_word = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]


print("Welcome to the password guessing game")
print("Choose a different level of difficulty: easy, medium, haed")


level = input("enter difficlty:").lower()
if level == "easy":
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_word)
    
    
                
    

             
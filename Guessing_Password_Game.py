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
    
attempts = 0
print("\Guess the secret password")

while True:
    guess =input("enter your guess: ").lower() 
    attempts += 1
    
    if guess == secret:
        print(f'Congratulations! You guessed it in {attempts} attempts.') 
        break
    
    
    hint = ""
    
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
            
    print("Hint: ", hint)
print("Game Over! The secret password was:", secret)            
      
    
    
                
    

             
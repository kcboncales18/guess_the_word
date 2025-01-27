import random 

# Words that can be guessed 
words = ["apple", "banana", "programming", "tiger", "lamp", "television", "projects", "water",
         "cake", "flower", "car", "clouds", "pencil", "dress", "watch", "cat", "paper"]

# Randomly choose a word
random_word = random.choice(words)

print("GUESS THE WORD".center(30, "*"))
print("Hint: the word has", len(random_word), "letters.")

user_guesses = ''
chances = 5 

while chances > 0: 
    wrong_guesses = 0 

    for character in random_word:
        if character in user_guesses: 
            print(f"Correct guess:{character}")  
        else:
            wrong_guesses += 1 
            print("_")


   
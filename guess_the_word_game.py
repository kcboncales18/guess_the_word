import random 

#words that can be guessed 
words = ["apple", "banana", "programming","tiger", "lamp", "television", "projects", "water",
         "cake", "flower", "car","clouds", "pencil", "dress", "watch", "cat", "paper"]

random_words = random.choice(words)

print("GUESS THE WORD".center(30, "*"))
import random

# List of words for the game
words = ["apple", "banana", "cherry", "grape", "orange", "mango", "peach"]

# Randomly select a word from the list
selected_word = random.choice(words)

print("Welcome to the Guess the Word Game!")
print("I have selected a word from the list. Try to guess it!")

# Loop until the user guesses the word correctly
while True:
    guess = input("Enter your guess: ").strip().lower()
    
    if guess == selected_word:
        print("Congratulations! You guessed the word correctly!")
        break
    else:
        print("Incorrect guess. Try again!")

print("Thank you for playing!")

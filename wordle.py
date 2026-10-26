import random

NUM_ATTEMPTS = 6

WORDS = ["apple", "grape", "house", "plant", "smile", "brain", "chair", "dream", "flame", "stone","bread", "cloud", "dance", "earth", "fruit", "green", "light", "music", "ocean", "peace","drive", "teach", "solve", "check", "guess", "match", "score", "level", "bonus", "prize", "clear", "clean", "baby", "human", "blood", "brain", "nerve", "organ", "cells"]

def main():
    print("Welcome to Wordle!")

    secret_word = random.choice(WORDS)

    for attempt in range(NUM_ATTEMPTS):
        guess = input("Enter your guess: ")
        guess = guess.lower()
    
        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ")
            guess = guess.lower()
    

        result = []
        remaining_letters = list(secret_word)

        for i in range(5):
            if guess[i] == secret_word[i]:
                result.append("G")
                remaining_letters.remove(guess[i])
            else:
                result.append("B")

        for i in range(5):
            if result[i] == "B" and guess[i] in remaining_letters:
                result[i] = "Y"
                remaining_letters.remove(guess[i])

        formatted_result = []

        for i in range(5):
            if result[i] == "G":
                formatted_result.append("[" + guess[i] + "]")
            elif result[i] == "Y":
                formatted_result.append("(" + guess[i] + ")")
            else:
                formatted_result.append(guess[i])

        print("Result:", " ".join(formatted_result))

        if guess == secret_word:
            print(f"Congratulations! You guessed the word in {attempt + 1} tries!")
            break
    else:
        print(f"Better luck next time! The correct word was '{secret_word}'.")

if __name__ == "__main__":
    main()
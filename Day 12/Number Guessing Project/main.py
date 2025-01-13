from art import logo
import random

print(logo)
print("Welcome to the number guessing Game !")
print("I'm thinking of a number between 1 and 100")


def play_game():
    secret_number = random.randint(1, 100)
    difficulty = input("Please choose a difficulty easy or hard: ").lower()
    playing = True
    guess = int
    attempts_e = 10
    attempts_h = 5
    while playing:
        if difficulty == "easy":
            print(f"attempts remaining: {attempts_e}")
            guess = int(input(f"Make a guess: "))
            if guess != secret_number:
                attempts_e -= 1
                if attempts_e == 0:
                    playing = False
                    print("Sorry You lost")

        elif difficulty == "hard":
            print(f"attempts remaining: {attempts_h}")
            guess = int(input(f"Make a guess: "))
            if guess != secret_number:
                attempts_h -= 1
                if attempts_h == 0:
                    playing = False
                    print("Sorry You lost")

        if guess < secret_number:
            print("Too low ")
        elif guess > secret_number:
            print("Too high")
        elif guess == secret_number:
            print(f"you got it! the Answer was {secret_number}")
            playing = False


play_game()

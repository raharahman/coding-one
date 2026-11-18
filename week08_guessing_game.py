#guessing game, with list
import random

def guessing_game():
    secret = random.randint(1,50)
    guesses = []
    while True:
        guess = int(input("Guess (1-50): "))
        if len(guesses) == 0 or guess != guesses[-1]:
            guesses.append(guess)
        if guess > secret:
            print("Too large!")
        elif guess < secret:
            print("Too small!")
        else:
            print(f"Correct! {len(guesses)} tries: {guesses}")
            break

def print_box(message, corner):
    line = corner + "-" * (len(message) +2) + corner
    print(line)
    print("| " + message + " |")
    print(line)

def chat():
    corner1 = input("Player 1, pick a corner character: ")
    corner2 = input("Player 2, pick a corner character: ")
    for turn in range(2):
        print_box(input("Player 1: "), corner1)
        print_box(input("Player 2: "), corner2)

choice = input("Play: 1) guessing game 2) chat boxes : ")
if choice == "1":
    guessing_game()
else:
    chat()
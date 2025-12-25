import random

num = random.randint(1,100)

while True:
    guess = int(input("Guess the number "))

    if num == guess :
        print("you guess the number ")
        break

    if num > guess:
        print("Guess is too loo")
    elif num < guess:
        print("Guess is too high")
    else:
        print("Invalid input")

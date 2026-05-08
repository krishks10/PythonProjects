import random

print("===Welcome to Number Guessing Game===")

top_of_range = input("Type a number")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print("Please Type a larger number than zero next time.")
        quit()
else:
    print("Please type a number ")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1

    user_guess = input("Type a Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time")

    if user_guess == random_number:
        print("You got it!")
        break
    
    if user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in ", guesses, "guesses")
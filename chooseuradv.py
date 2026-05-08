name = input("Enter your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right.\n Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across?\nType walk to walk around or swim to swim across: ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer =="walk":
        print("You walked for many miles, ran out of the water and you lost the game.")
    else:
        print("Not a valid option, you lose.")

elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross a bridge and meet a stranger. do you talk to them(yes/no)? ")
        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print("Not a valid option, You Lose.")
else:
    print("Not a valid option, You Lose.")

print("Thank You for trying", name)
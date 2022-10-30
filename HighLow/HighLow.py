import random

print("This is a High Low game made in Python!")

def start():
    success = False
    print("Try to guess a number between 0 and 50 in 10 tries.")
    number = random.randrange(0, 50)
    for x in range (10):
        guess = int(input("Enter your guess: \n"))
        if(guess == number):
            success = True
            break
        else:
            print("Low") if guess < number else print("High")

    print("You got the number!") if success == True else print("You failed :<")
    again = input("Want try again? Y/N \n")
    start() if again.upper()=="Y" else (print("Alright, thanks for playing.") if again.upper()=="N" else print("Input not recognized. Finishing game anyway."))

start()

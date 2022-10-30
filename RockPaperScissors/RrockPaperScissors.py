import random

print("This is a Rock Paper Scissors game made in Python!")

def start():
    choices = ["ROCK", "PAPER", "SCISSORS"]

    win = False
    
    while True:
        randchoice = random.choice(choices)
        choice = input("Enter your choice: Rock, Paper or Scissors? \n").upper()
        if(choice == randchoice): 
            print("There was a tie") 
            continue
        if(choice not in choices):
            print("Invalid response, try again.")
            continue
        if(choice == "ROCK" and randchoice == "SCISSORS"):
            win = True
            break
        if(choice == "PAPER" and randchoice == "ROCK"):
            win = True
            break
        if(choice == "SCISSORS" and randchoice == "PAPER"):
            win = True
            break
        break

    print("You win!") if win else print("You lose :<")
    again = input("Want try again? Y/N \n")
    start() if again.upper()=="Y" else (print("Alright, thanks for playing.") if again.upper()=="N" else print("Input not recognized. Finishing game anyway."))

start()

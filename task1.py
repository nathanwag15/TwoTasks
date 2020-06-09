#Number Guessing Game
#Nathan Wagstaff
#2/13/2020

#CS-1400

#intro
print("Welcome to the Guessing Game")
print("The Computer has picked a number from 1-10. Try to match it.")

#number generaton
from random import randint
answer= randint(1,10)

#user input
user = int(input("What number do you choose (1-10): "))

#answers
msg = f"You picked {user}, and the actual number was {answer}. \n"

#off
if user == answer - 1 or user == answer + 1:
    msg += "You are a worthy opponent, Knight."
if user == answer - 2 or user == answer + 2:
    msg += "You have much to learn, Padawan."
if user == answer - 3 or user == answer + 3:
    msg += "Youngling your time will come."
if user < answer - 3 or user > answer + 3:
    msg += "Keep working hard in the Service Corps."

print(msg)
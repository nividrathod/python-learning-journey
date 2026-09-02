# Simple User VS Computer Rock Paper Scissors Game

import random

user_choice = input("Enter your move [Rock, Paper, Scissor]: ").capitalize()

items = ["Rock", "Paper", "Scissor"]
comp_choice = random.choice(items)

print(f"\nYou Chose: {user_choice}")
print(f"Computer Chose: {comp_choice}")

if user_choice == comp_choice:
    print("\nResult: Match is Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("\nResult: Computer Wins!")
        print("Remark: Paper covers Rock.")
    else:
        print("\nResult: User Wins!")
        print("Remark: Rock smashes Scissor.")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("\nResult: User Wins!")
        print("Remark: Paper covers Rock.")
    else:
        print("\nResult: Computer Wins!")
        print("Remark: Scissor cuts Paper.")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("\nResult: User Wins!")
        print("Remark: Scissor cuts Paper.")
    else:
        print("\nResult: Computer Wins!")
        print("Remark: Rock smashes Scissor.")

else:
    print("\nInvalid Choice! Please choose Rock, Paper, or Scissor.")

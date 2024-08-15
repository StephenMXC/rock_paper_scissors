import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


possibilities = ["rock", "paper", "scissors"]
computer = random.choice(possibilities)
user = input("Choose your hand. \n ").lower()


if user == computer:
    print(f"You chose: {user}\n Computer chose: {computer}\n It's a draw!")
elif user == "rock":
    if computer == "paper":
        print(f"You chose: {rock} \n Computer chose:{paper} \n You lose.")
    else:
        print(f"You chose:{rock} \n Computer chose:{scissors} \n You win.")
elif user == "paper":
    if computer == "rock":
        print(f"You chose:{paper} \n Computer chose:{rock} \n You win.")
    else:
        print(f"You chose:{paper} \n Computer chose:{scissors} \n You lose.")
elif user == "scissors":
    if computer == "rock":
        print(f"You chose:{scissors} \n Computer chose:{rock} \n You lose.")
    else:
        print(f"You chose:{scissors} \n Computer chose:{paper} \n You win.")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_sign=[rock,paper,scissors]
user_num= int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(game_sign[user_num])
print("The Computer chose:\n")
comp_num=random.randint(0,2)
print(game_sign[comp_num])
if user_num==0:
    if comp_num==0:
        print("Tie, Try Again")
    elif comp_num==1:
        print("You Lose")
    elif comp_num==2:
        print("You Win")
    else:
        print("Wrong Input")

elif user_num==1:
    if comp_num==0:
        print("You Win")
    elif comp_num==1:
        print("Tie, Try Again")
    elif comp_num==2:
        print("You Lose")
    else:
        print("Wrong Input")

elif user_num==2:
    if comp_num==0:
        print("You Lose")
    elif comp_num==1:
        print("You Win")
    elif comp_num==2:
        print("Tie, Try Again")
    else:
        print("Wrong Input")
else:
    print("Wrong Input,Try Again")

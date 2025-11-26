import random
item_list=["Rock","Paper","Scissors"]
user_choice=input("Enter your Move :!\nRock\nPaper\nScissors\n")
computer_choice =random.choice(item_list)
print(f"User choice : {user_choice}")
print(f"Computer_choice :{computer_choice}")
if user_choice==computer_choice:
    print("Both choose the same :( Match Tie")
elif user_choice=="Rock":
    if computer_choice=="Paper":
       print("Paper Covers Rock :( Computer Wins :((")
    else:
        print("Rock smashes Scissors :) YAYAAYYY You win !! :))")

elif user_choice=="Paper":
    if computer_choice=="Scissors":
        print("Oh no scissors take over paper :( Computer wins :((")
    else :
        print("Paper covers Rock ! You win :))")

elif user_choice=="Scissors":
    if computer_choice=="Rock":
        print("NOOO Rock takes over scissors :( Computer wins :((")
    else:
        print("YAYAYA You win ! :))")    





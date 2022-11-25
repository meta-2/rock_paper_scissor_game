import random

Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
done = True
def game():
    global done
    while done:
        game_image=[Rock,Paper,Scissors]
        user_choice = int(input("you can select 0 for rock, 1 for paper and 2 for Scissors"))
        if user_choice >= 3:
            print("you select wrong option , you lose!")
        else:
            print("user choice")
            print(game_image[user_choice])
            computer_choice=random.randint(0,2)
            print(f"computer choice {computer_choice}")
            print(game_image[computer_choice])
            if user_choice == computer_choice:
                print("draw")
                done = False
            elif user_choice == 2 and  computer_choice == 1:
                print("you win")
                done = False
            elif user_choice == 0 and computer_choice == 2:
                print("you win")
                done = False
            elif user_choice == 1 and  computer_choice == 0:
                print("you win")
                done = False
            elif user_choice == 2 and computer_choice == 0:
                print("you win")
                done = False
            else:
                print("you lose")
                done = False


game()

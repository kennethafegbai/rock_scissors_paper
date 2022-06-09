import random

# while True:
#     user_choice = input("Enter a choice (rock, paper, scissors): \n")
#     possible_choices = ["rock", "paper", "scissors"]
#     if user_choice not in possible_choices:
#         print('---Your input is wrong!!!--- \n Try again..')
#         exit()
#     computer_choice = random.choice(possible_choices)
#     print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
#     if user_choice == computer_choice:
#         print(f"Both players selected {user_choice}. It's a tie!")
#     elif user_choice == "rock":
#         if computer_choice == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_choice == "paper":
#         if computer_choice == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_choice == "scissors":
#         if computer_choice == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

#     play_again = input("Play again? (y/n): \n")

#     if play_again.lower() != "y":
#         break

def rock_scissors_paper():
    while True:
        user_choice = input("Enter a choice (R, P, S): \n").upper()
        possible_choices = ["R", "P", "S"]
        possible_choices_value = {"R":'Rock', "P":"Paper", "S":"Scissors"}

        if user_choice not in possible_choices:
            print('---An error occurred!!!--- \n')
            try_again = input("Do you want to try again? (y/n)").lower()
            if(try_again == 'y'):
                rock_scissors_paper()
            else:
                break
        computer_choice = random.choice(possible_choices)
        print(f"\nPlayer({possible_choices_value[user_choice]}):CPU({possible_choices_value[computer_choice]}).\n")
        if user_choice == computer_choice:
            print(f"It's a tie!(both players selected {possible_choices_value[user_choice]})")
        elif user_choice == "R":
            if computer_choice == "S":
                print("Rock beats scissors!")
            else:
                print("Paper beats rock!")
        elif user_choice == "P":
            if computer_choice == "R":
                print("Paper beats rock!")
            else:
                print("Scissors beats paper!")
        elif user_choice == "S":
            if computer_choice == "P":
                print("Scissors beats paper!")
            else:
                print("Rock beats scissors!")

        play_again = input("\nWant to start again? (y/n): \n")
        

        if play_again.lower() != "y":
            break

rock_scissors_paper()
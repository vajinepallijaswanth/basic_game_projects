import random
game = ['rock', 'paper', 'scissor']
print("Enter number to choose")
user_choice = int(input("0: Rock, 1: Paper, 2: Scissor, 3:Exit Game "))

while user_choice == 1 or user_choice == 2 or user_choice == 0:
     print(f"You choosed: {game[user_choice]} ")
     computer_choice = random.randint(0,2)
     print(f"Computer choosed: {game[computer_choice]}")
     if computer_choice == user_choice:
        print("It's Draw")
     elif computer_choice == 0 and user_choice == 2:
        print("You Loose")
     elif user_choice == 0 and computer_choice == 2:
        print("You Win")
     elif computer_choice > user_choice:
        print("You Loose")
     elif user_choice > computer_choice:
        print("you win")
     user_choice = int(input("0: Rock, 1: Paper, 2: Scissor,3:Exit Game "))
else:
    while user_choice != 3:
        print("You entered invalid number, You Loose...")
        user_choice = int(input("0: Rock, 1: Paper, 2: Scissor,3:Exit Game "))
        while user_choice == 1 or user_choice == 2 or user_choice == 0:
            print(f"You choosed: {game[user_choice]} ")
            computer_choice = random.randint(0, 2)
            print(f"Computer choosed: {game[computer_choice]}")
            if computer_choice == user_choice:
                print("It's Draw")
            elif computer_choice == 0 and user_choice == 2:
                print("You Loose")
            elif user_choice == 0 and computer_choice == 2:
                print("You Win")
            elif computer_choice > user_choice:
                print("You Loose")
            elif user_choice > computer_choice:
                print("you win")
            user_choice = int(input("0: Rock, 1: Paper, 2: Scissor,3:Exit Game "))
    else:
        while user_choice == 3:
            print("Game exit...")
            break




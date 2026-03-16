import random

print("----Rock Paper Scissors Game ----")

user_score = 0
computer_score = 0

while True:

    user = input("Enter rock,paper or scissors: ").lower()

    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)

    print("You chose: ",user)
    print("Computer chose: ",computer)

    if user == computer:
        print("It's a tie")

    elif user == "rock" and computer == "scissors":
        print("You win!")
        user_score = user_score + 1

    elif user == "scissors" and computer == "paper":
        print("You win!")
        user_score = user_score + 1

    elif user == "paper" and computer == "rock":
        print("You win!")
        user_score = user_score + 1

    else:
        print("Computer wins!")
        computer_score = computer_score + 1


    print("User score: ",user_score)
    print("Computer Score: ",computer_score)

    again = input("Play again? (yes/no): ")

    if again == "no":
        print("---Game Over---")
        break




    

import random

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("Computer chose:", computer_choice)
    print("You chose:", user_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1

    else:
        print("You lose!")
        computer_score += 1

    # Show score after every round
    print("Your score:", user_score)
    print("Computer score:", computer_score)

    # Check winner
    if user_score == 3:
        print("🎉 Congratulations! You won the game!")
        break
    elif computer_score == 3:
        print("💻 Computer won the game!")
        break

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        print("Thanks for playing!")
        break
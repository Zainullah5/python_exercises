import random 

while True:
    num = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == num:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Wrong guess! The correct number was {num}. Better luck next time!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break
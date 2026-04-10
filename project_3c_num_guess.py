# Author: James Harris
# GitHub username: thestackman
# Date: 04102026
# Description:  Get a number from the user and allow a player to guess the number, giving hints until correct answer is entered.

# Get user input
print("Enter the integer for the player to guess.")
num_to_guess = int(input())

print("Enter your guess.")
player_guess = int(input())

guess_count = 1

# Compare player guess to user number - print hints and message when true
if player_guess == num_to_guess:
    print(f"You guessed it in {guess_count} try.")

else:
    while player_guess != num_to_guess:
        if player_guess < num_to_guess:
            print("Too low - try again:")
            player_guess = int(input())
            guess_count += 1

        elif player_guess > num_to_guess:
            print("Too high - try again:")
            player_guess = int(input())
            guess_count += 1

    print(f"You guessed it in {guess_count} tries.")

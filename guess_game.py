import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number I am thinking of between 1 and 100.")

    # Loop until the guess is correct
    while guess != secret_number:
        try:
            # Get user input and convert to integer
            guess_str = input("Enter your guess: ")
            guess = int(guess_str)

            # Provide feedback
            if guess < secret_number:
                print("Too low, try again.\n")
            elif guess > secret_number:
                print("Too high, try again.\n")
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # This part is reached when the while loop breaks (guess is correct)
    print(f"Congratulations! You guessed the number {secret_number} correctly!\n")

if __name__ == "__main__":
    number_guessing_game()

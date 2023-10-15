import random

def get_user_input():
    while True:
        try:
            a = int(input("Enter the lower limit of the range: "))
            b = int(input("Enter the upper limit of the range: "))
            if a >= b:
                print("The lower limit should be less than the upper limit. Please try again.")
                continue
            return a, b
        except ValueError:
            print("Invalid input. Please enter integer values.")

def number_guessing_game():
    a, b = get_user_input()
    print(f"I have selected a number between {a} and {b}. Can you guess it?")
    secret_number = random.randint(a, b)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    number_guessing_game()
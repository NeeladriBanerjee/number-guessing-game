import random

def guess():
    print("Welcome to the Number Guessing Game!")
    
    # Get custom range from user with input validation
    while True:
        try:
            min_num = int(input("Enter the minimum number: "))
            max_num = int(input("Enter the maximum number: "))
            
            if min_num >= max_num:
                print("The maximum number must be greater than the minimum number. Try again.\n")
                continue
            break
        except ValueError:
            print("Please enter valid integers for the range.\n")

    # Generate a random integer within the chosen range
    num = random.randint(min_num, max_num)
    attempt = 0
    
    print(f"\nI've chosen a random number between {min_num} and {max_num}. Start guessing!")

    # Guessing loop
    while True:
        try:
            val = int(input("Enter your guess: "))
            attempt += 1
            
            if val < min_num or val > max_num:
                print(f"Out of bounds! Guess a number between {min_num} and {max_num}.")
            elif val < num:
                print("Low, try higher.")
            elif val > num:
                print("High, try lower.")
            else:
                print(f"You guessed it correctly in {attempt} attempts!")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Start the game
guess()
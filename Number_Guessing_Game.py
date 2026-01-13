import random

while True:
    guess_number = random.randint(1, 10)
    user_guess = int(input("Enter a number 1 - 10: "))
    
    if user_guess > guess_number:
        print(f"{user_guess} too high...")
        continue
    
    elif user_guess < guess_number:
        print(f"{user_guess} too low...")
        continue
        
    else:
        print(f"{user_guess} equal {guess_number}")

    again = input("Do you want to try another number (yes/no) ").lower()
    if again != "yes":
        print("Goodbye")
        break
import random

print("I guess your imaginary number!\nPlease anwser with \"yes\" or \"no\".\n")

input("When you imagine your number, press Enter to start the game!\n")

first = 1
second = 100
attempts = 1

while True:
    try:
        guess = random.randint(first, second)
    except ValueError:
        print("\nYou liar!!")
        break

    answer = input(f"Is your imagine number {guess}? ").lower()
    if answer == "yes":
        print(f"\nI guessed your number in {attempts} attempts.")
        input("\nPress Enter to exit..")
        exit()
    elif answer == "no":
        attempts += 1
        if guess > first:
            question = input(f"Is your number less than {guess}? ").lower()
            if question == "yes":
                second = guess - 1
                    
            elif question == "no":
                first = guess + 1
            else:
                print("Please Enter yes or no.")

    else:
        print("Please Enter yes or no.")

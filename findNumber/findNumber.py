import random

if __name__ == '__main__':
    lower_limit, upper_limit = 1, 30
    random_int = random.randint(lower_limit, upper_limit)

    num_of_guesses = 0

    while True:
        user_guess = input("Your guess (int), or 'exit':")
        if user_guess == "exit":
            print("Exiting...")
            break

        try:
            user_guess = int(user_guess)
        except ValueError:
            print(f"Please use ints. Your input: {user_guess}.")
            continue

        print(f"Your guess {user_guess}.")
        num_of_guesses += 1
        if user_guess == random_int:
            print(f"You guess is exactly right.")
            break
        elif user_guess > random_int:
            print(f"Your guess is too high.")
        elif user_guess < random_int:
            print(f"Your guess is too low.")

    result_text = f"Thanks for playing! You tried {num_of_guesses} times."
    print(result_text)

    file = open("GuessingSteps.txt", mode="a")
    print(result_text, file=file)
    file.close()


secret_word = "corona virus"
user_guess = ""
guess_counter = 0
out_of_guesses = False

while user_guess != secret_word and not out_of_guesses:
    if guess_counter < 3:
        user_guess = input("Enter the secret word: ")
        guess_counter += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You LOSE !")
else:
    print("You WIN !")

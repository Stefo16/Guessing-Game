
secret_pair = "76"
guess = ""
guess_count = 0
guess_limit = 10
out_of_guesses = False

while guess != secret_pair and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Pick any two digit number: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You ran out of guess attempts, You LOSE!")
else:
    print("You WIN! You guessed a total of "+ str(guess_count)+" times.")





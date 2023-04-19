secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_number = int(input("Guess: "))
    guess_count += 1
    if guess_number ==  secret_number:
        print("you guess is correct")
        break
else:
    print("your guess is wrong")
secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess A Number: "))
    guess_count += 1
    if guess == secret_number:
        print("Congrats, You Won!!")
        break
else:
    print("Sorry, You Failed")

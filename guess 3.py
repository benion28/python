count = 0
guess_number = 8
guess_limit = 3


def check_name_type(name):
    if name.isalpha():
        print(f"Welcome {user_name.upper()}")
        return True
    else:
        print("Name Must Be All Alphabets")
        return False


while True:
    user_name = input("Input Your Name: ")
    is_checked = check_name_type(user_name)
    if is_checked:
        break


while count < guess_limit:
    guess = ""
    try:
        guess = int(input("Guess A Number: "))
    except ValueError:
        print("Error, Input Must Be An Integer")
    if guess == guess_number:
        print(f"Your Guess ({ guess }) Is Correct")
        break
    else:
        if count == 0:
            print("Wrong Guess, 1st Attempt")
        elif count == 1:
            print("Wrong Guess, 2nd Attempt")
        elif count == 2:
            print("Sorry You Tried 3 Times And Failed")
        count += 1

count = 0
guess_number = 8
guess_limit = 3

def check_name_type(name):
    if name.startswith("0"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("1"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("2"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("3"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("4"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("5"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("6"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("7"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("8"):
        print("Name Must Be Alphabets")
        return False
    elif name.startswith("9"):
        print("Name Must Be Alphabets")
        return False
    else:
        print(f"Welcome { user_name.upper() }")
        return True


while True:
    user_name = input("Input Your Name: ")
    is_checked = check_name_type(user_name)
    if is_checked == True:
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

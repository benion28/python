name = input("Enter Your Name: ")
if len(name) < 3:
    print("Name Should Be At Least 3 Characters")
elif len(name) > 50:
    print("Name Should Be Maximum Of 50 Characters")
else:
    print("Name Looks Good")
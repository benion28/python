try:
    age = int(input("Age: "))
    print(age)
    income = 20000
    risk = income // age
    print(risk)
except ZeroDivisionError:
    print("Age Cannot Be Zero(0)")
except ValueError:
    print("Invalid Number")

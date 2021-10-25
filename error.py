try:
	age = int(input("Age: "))
	print(f"Age is {age}")
	income = 20000
	risk = income // age
	print(f"Risk is {risk}")
except ZeroDivisionError:
	print("Age Cannot Be Zero(0)")
except ValueError:
	print("Invalid Number")


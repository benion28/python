full_name = input('Pls enter your full name')
age = int(input('pls enter your age'))
year = 2020
dob = year - age
format = 'e.g 1st, Dec'
print(f'Hi, {full_name} Welcome to vin program')
print(f'your year of birth is {dob}')
day_and_month = input(f'Pls enter your day and month of birth in this format {format}')
date_of_birth = f'{day_and_month} {dob}'
print(date_of_birth)
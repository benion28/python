import random
import string

alphabets = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation
total = int(input("Total Password: "))
password = ''

for index in range(total):
    if index == 0:
        password += password.join(random.sample(alphabets.upper(), 1))
    elif 0 < index < 4:
        password += password.join(random.sample(alphabets, 1))
    elif 3 < index < 7:
        password += password.join(random.sample(numbers, 1))
    else:
        password += password.join(random.sample(symbols, 1))

print(password)

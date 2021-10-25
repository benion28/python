number = input("Type In Numbers: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for character in number:
    output += digit_mapping.get(character, "Unknown") + " "
print(output)

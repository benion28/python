import pandas as pd

data = pd.read_csv("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\tree-diameter-height.csv")
data.shape


# from random import randrange
# items = []
#
# for count in range(180):
#     number = randrange(450)
#     present = False
#     if len(items) == 0:
#         items.append(number)
#     for item in items:
#         if item == number:
#             present = True
#     if not present and len(items) < 90:
#         items.append(number)
#         present = False
#
#
# print(items)
# print(f"We have {len(items)} Items")

from tkinter import font

num1 = 21
list2 = [1, 0, 0, 0, 0]
list3 = [1, 1, 1, 1, 1]


print(all(list2))










# for index in range(num1):
#     list3.append((index + 1) * list2[index % len(list2)])
# print(list3)
#
# nearest_columns_to_fill = 0
# list4 = []
#
# for index, item in enumerate(list3):
#     if item != 0:
#         nearest_columns_to_fill += 1
#         pass
#     if item == 0:
#         list4.append(nearest_columns_to_fill)
#         if list4[-1] != 0: list4.append(0)
#         nearest_columns_to_fill = 0
#
# print(list4)
#
#
# #print(list[a % 7 - 1])
#
# list3 = []
# for index in range(columns):
#     list3.append((index + 1) * days_set[index % len(days_set)])
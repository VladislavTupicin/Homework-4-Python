# Номер 1

# count = int(input('Введите количество элементов: '))
# some_list = []
# sum = 0
# for _ in range(count):
#     number = int(input())
#     some_list.append(number)
# for idx in range(1, count, 2):
#     sum += some_list[idx]
# print(sum)







# Номер 2

# count = int(input('Введите количество элементов: '))
# some_list = []
# for _ in range(count):
#     number = int(input())
#     some_list.append(number)
# new_list = []
# for idx in range((count - 1) // 2 + 1):
#     number1 = some_list[idx]
#     number2 = some_list[count - idx - 1]
#     new_list.append(number1 * number2)
# print(new_list)







# Номер 3

# count = int(input('Введите количество элементов: '))
# some_list = []
# for _ in range(count):
#     number = (input())
#     some_list.append(number)
# min = 1
# max = 0
# for el in some_list:
#     if '.' in str(el):
#         dr = str(el).split('.')[1]
#         if float('0.' + dr) > max:
#             max = float('0.' + dr)
#         elif float('0.' + dr) < min:
#             min = float('0.' + dr)
# print(max - min)






# Номер 4

# a = int(input())
# print(bin(a)[2:])





# Номер 5

# k = int(input())
# some_list = [0] * (k * 2 + 1)
# some_list[k + 1] = 1
# for idx in range(k + 2, k * 2 + 1):
#     some_list[idx] = some_list[idx - 1] + some_list[idx - 2]
# for idx in range(k, -1, -1):
#     some_list[idx] = some_list[idx + 2] - some_list[idx + 1]
# print(some_list)
number = [9, 58, 45, 32, 12, 37, 1, 9, 2, 3, 4, 5, 11, 16]
n = len(number)
while n > 1:
    for i in range(n - 1):
        if number [i] > number [i + 1]:
            number [i], number [i + 1] = number [i + 1], number [i]
    n -= 1
print("Sorted numbers:", number)


my_list = [9, 58, 45, 32, 12, 37, 1, 9, 2, 3, 4, 5, 11, 16]
my_list.sort()

print( my_list)
    
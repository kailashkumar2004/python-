list = [1, 2, 4, 8, 9, 80, 75, 64, 31, 87, 80, 4, 3, 1, 99, 67, 75]
uniqueNumbers = []
for number in list:
    if number not in uniqueNumbers:
        uniqueNumbers.append (number)
print("Unique numbers:", uniqueNumbers)



number=[12,90,86,43,67,89,1,3,4,5,6,7,8,9,12,90,86,8,9,1]
uniqueNumbers=[]

for number in number:
    if number not in uniqueNumbers:
        uniqueNumbers.append(number)
print(uniqueNumbers)        
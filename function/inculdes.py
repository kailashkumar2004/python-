def num():
    num1=[1,3,6,8,9,11,21,32,35,67,89,90,86,54,321]
    num2=[45,78,90,12,34,56,87,89,21,11,19,20,1,3]
    same_numbers=set(num1).intersection(num2)
    print(same_numbers)
num()    
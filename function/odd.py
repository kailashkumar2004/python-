# def num():
#     num=int(input("enter the any num=================="))
#     i=1
#     while i<=num:
#         if i%2!=0:
#             print(i,"odd")
#         i=i+1    
# num()   

# def number():
#     list=[1,9,2,3,8,11,19,87,43,56,78,90,91,81,71,61,15] 
#     i=0
#     while i<len(list):
#         if list[i]%2!=0:
#             print(list[i],"odd")
#         i=i+1    
# number()               


def number(num):
    i=0
    while i<len(num):
        if num[i]%2!=0:
            print(num[i],"odd")
        i=i+1  
num=[1,2,3,4,5,6,7,8,9,10,11]          
number(num)        
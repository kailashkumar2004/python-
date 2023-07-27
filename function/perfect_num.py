# def num():
#     num=6
#     i=1
#     sum=0
#     while i<num:
#         if num%i==0:
#             sum=sum+i
#         i=i+1
#     if sum==num:
#         print(num,"sum is a perfect number") 
#     else:
#         print(num,"sum is a not perfect number")
# num()           

def number():
    num=int(input("enter the any num============="))
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if sum==num:
        print(sum,"sum is a perfect number")
    else:
        print(sum,"sum is a not perfect number")    
number()           
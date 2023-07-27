def number():
    num=int(input("enter the any num============="))
    i=1
    while i<=num:
        if i%2==0:
            print(i,"even")
        i=i+1
number() 

def num():
    list=[1,2,3,4,5,6,7,8,9,10]
    i=0
    while i<len(list):
        if list[i]%2==0:
            print(list[i],"even")
        i=i+1          
num()        
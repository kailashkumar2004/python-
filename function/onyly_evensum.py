def num():
    num=int(input("enter the any num==========="))
    i=1
    evensum=0
    while i<=num:
        if i%2==0:
            evensum=evensum+i
        i=i+1    
    print("total of evensum",evensum)
num()

def  number():
    list=[11,23,56,43,22,54,67,89,65,18,20,30,86,46,90]
    i=0
    evensum=0
    while i<len(list):
        if list[i]%2==0:
            evensum=evensum+list[i]
        i=i+1
    print("total of evensum",evensum)        
number()    
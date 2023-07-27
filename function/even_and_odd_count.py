def number():
     num=int(input("enter the any num====================="))
     i=1
     evencount=0
     oddcount=0
     while i<=num:
         if i%2==0:
             evencount=evencount+1
         else:
             oddcount=oddcount+1
         i=i+1
     print("total of evencount",evencount) 
     print("total of oddcount",oddcount)       
number()   


def num():
    list=[2,5,6,7,8,9,11,21,23,34,56,65,76,67,87,78,98,89]
    i=0
    evencount=0
    oddcount=0
    while i<len(list):
        if list[i]%2==0:
            evencount=evencount+1
        else:
            oddcount=oddcount+1
        i=i+1
    print("total of evencount",evencount) 
    print("total of oddcount",oddcount)
num()               
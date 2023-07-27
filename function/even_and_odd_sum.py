def number():
    num=int(input("enter the any num==================="))
    i=0
    evensum=0
    oddsum=0
    while i<=num:
        if i%2==0:
            evensum=evensum+i
        else:
            oddsum=oddsum+i
        i=i+1
    print("total of evensum",evensum)
    print("total of oddsum",oddsum)
number()                    


def num():
    list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    evensum=0
    oddsum=0
    i=0
    while i<len(list):
        if list[i]%2==0:
            evensum=evensum+list[i]
        else:
            oddsum=oddsum+list[i] 
        i=i+1
    print("total of evensum",evensum) 
    print("total of oddsum",oddsum)   
num()               
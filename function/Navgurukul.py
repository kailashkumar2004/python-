def num():
    num=100
    i=1
    while i<=num:
        if i%3==0 and i%7==0:
            print(i,"navgurukul")
        elif i%7==0:
            print(i,"gurukul")
        elif i%3==0:
            print(i,"nav")
        else:
            print(i) 
        i=i+1 
num()  


def number():
    num=int(input("enter the any num====================="))
    i=1
    while i<=num:
        if i%3==0 and i%7==0:
            print(i,"navgurukul")
        elif i%7==0:
            print(i,"gurukul")
        elif i%3==0:
            print(i,"nav")
        else:
            print(i) 
        i=i+1               
number()                            
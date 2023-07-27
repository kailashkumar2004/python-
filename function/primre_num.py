def num():
    num=int(input("enter the any num================"))
    i=2
    count=0
    while i<=num:
        if num%i==0:
            count=count+1
        i=i+1
    print("count============",count)
    if count==1:
        print("this is a prime number")
    else:
        print("this is a not prime number")     
num()       
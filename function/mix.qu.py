# def num():
#     a=90
#     b=80
#     print(a+b)
# num()    

# def number(num1,num2):
#     num3=90
#     if num1>num2 and num1>num3:
#         print("first condation is a ture")
#     elif num1<num2 and num2<num3:
#         print("secoun condation is a ture")
#     elif num1==num2 and num2>=num3:
#         print("third condation is a ture") 
#     else:
#         print("fallse condation")           
    
# number(70,80)    

# def num():
#     list=[90,76,54,32,87,100,36]
#     max=list[0]
#     i=0
#     while i<len(list):
#         if list[i]>max:
#             max=list[i]
#         i=i+1
#     print(max)
# num() 

# def num():
#     list=[2,5,7,9,65,34,57,90,21,22,32,43,54,36]
#     min=list[0]
#     i=0
#     while i<len(list):
#         if list[i]<min:
#             min=list[i]
#         i=i+1
#     print(min) 
# num()

# def num():
#     list=[1,2,3,4,5,6,7,8,9,11,21,32,34,56,76,87,98,89,90,76,1,3,2,4,5,6,7,8,9,11] 
#     uniqueNumber=[]
#     for number in list:
#         if number not in uniqueNumber:
#             uniqueNumber.append(number) 
#     print(uniqueNumber)
# num()                                

# def num():
#     num=100
#     i=1
#     while i<=num:
#         if i%3==0 and i%7==0:
#             print(i,"navgurukul")
#         elif i%7==0:
#             print(i,"gurukul")
#         elif i%3==0:
#             print(i,"nav")
#         else:
#             print(i) 
#         i=i+1 
# num()                      


# def number():
#     num=int(input("enter the any num====================="))
#     i=1
#     while i<=num:
#         if i%3==0 and i%7==0:
#             print(i,"navgurukul")
#         elif i%7==0:
#             print(i,"gurukul")
#         elif i%3==0:
#             print(i,"nav")
#         else:
#             print(i) 
#         i=i+1               
# number()        


# def num():
#     num=5
#     fact=1
#     while num>0:
#         fact=fact*num
#         num=num-1
#     print("fact",fact)    
# num()  




# def number():
#     num =int(input("enter the any num==================="))
#     fact=1
#     while num>0:
#         fact=fact*num
#         num=num-1
#     print(fact,"fact")     
# number()    


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

# def num():
#     num=int(input("enter the any num================"))
#     i=2
#     count=0
#     while i<=num:
#         if num%i==0:
#             count=count+1
#         i=i+1
#     print("count============",count)
#     if count==1:
#         print("this is a prime number")
#     else:
#         print("this is a not prime number")     
# num()       

# def navgurukul():
#     print("i am kailash")
#     print("i am form bihar")
# navgurukul()   

# def number(a,b):
#     c=a+b
#     print(c)
# number(10,20) 

# def number(num1,num2):
#     print(num1+num2) 
# number(20,20)    


# def number(a,b):
#     i=0
#     while i<len(a):
#         if a[i]%2==0 and b[i]%2==0:
#             print("both are even")
#         else:
#             print("not even") 
#         i=i+1
# a=[1,2,3,4,5,6,7,8] 
# b=[11,12,13,14,15,26]
# number(a,b)                

def vote():
    age=int(input("enter the any age=========="))
    if age>18:
        print("you are eligible hai")
    else:
        print("you are not eligible")
vote()            
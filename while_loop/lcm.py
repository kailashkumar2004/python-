num1=int(input("enter the any num1===================="))
num2=int(input("enter the any num2===================="))
i=1
lcm=0
while i>0:
    if i%num1==0 and i%num2==0:
        lcm=i
        break
    i=i+1
print(lcm)

a=10
b=14
i=1
lcm=0
while i>0:
    if i%a==0 and i%b==0:
        lcm=i
        break
    i=i+1
print(lcm)    
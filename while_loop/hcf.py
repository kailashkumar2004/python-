num1=int(input("enter the any num1==================="))
num2=int(input("enter the any num2===================="))
i=1
while i<=num1 and i<=num2:
    if num1%i==0 and num2%i==0:
         hcf=i
    i = i + 1
print(hcf)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

i = 1
while i <= num1 and i <= num2:
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
    i = i + 1

print("The highest common factor (HCF) is:", hcf)

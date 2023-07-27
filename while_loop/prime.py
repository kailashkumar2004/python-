num=int(input("enter the any num================"))
i=2
count=0
while i<=num:
    if num%i==0:
        count+=1
    i=i+1
print("count==================",count) 
if count==1:
    print("this is a prime number")
else:
    print("this is a not prime number")       
    
    
a=7
i=2
count=0
while i<=a:
    if a%i==0:
        count=count+1
    i=i+1
print ("count=============",count) 
if count ==1:
    print(count,"this is a perfect number") 
else:
   print (count,"this is a not perfect number")
   
x=11
i=2
count=0
while i<=x:
    if x%i==0:
        count=count+1
    i=i+1
print ("count=============",count) 
if count ==1:
    print(count,"this is a perfect number") 
else:
   print (count,"this is a not perfect number")
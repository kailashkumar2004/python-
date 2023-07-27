list=[1,0,0,1,1,0,1,1]
a=len(list )-1
sum=0
mult=1
while a>=0:
    sum=sum+(list[a]*mult)
    mult=mult*2
    a=a-1
print(sum) 
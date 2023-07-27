list=[1,12,34,54,31,23,67,89,88,96,58] 
evencount=0
oddcount=0
for i in list:
    if i%2==0:
        evencount=evencount +1
    else:
       oddcount =oddcount +1
print("total of evencount",evencount) 
print("total of oddcount",oddcount)
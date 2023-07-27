list=[1,2,3,4,5,6,7,8,9,10,11,21,13,46,78,90];
i=0
evencount=0
oddcount=0
while i<len(list):
    if list[i]%2==0:
        evencount=evencount +1
    else:
        oddcount=oddcount+1
    i=i+1 
print("total of evencount",evencount)  
print("total of oddcount",oddcount)


list=[21,10,19,29,38,47,56,78,90,11,17,22,39];
i=0
evencount=0
oddcount=0
while i<len(list):
    if list [i]%2==0:
        evencount=evencount+1
    else:
        oddcount=oddcount+1
    i=i+1
print("total of evencount",evencount)
print ("total of oddcount ",oddcount)
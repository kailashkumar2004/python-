list=[1,12,34,54,31,23,67,89,88,96,58] 
oddsum=0
for i in list:
    if i%2!=0:
        oddsum=oddsum+i
print("total of oddsum",oddsum)
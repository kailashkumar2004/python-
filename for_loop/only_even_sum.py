list=[1,12,34,54,31,23,67,89,88,96,58] 
evensum=0
for i in list:
    if i%2==0:
        evensum=evensum+i
print("total of evensum",evensum)
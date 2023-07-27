list=[2,4,6,5,7,8,9,12,13,14,15,16,1,89]
i=0
evensum=0
while i<len(list):
    if list[i]%2==0:
        evensum=evensum+list[i]
    i=i+1 
print("total of evensum",evensum)       


number=[11,24,34,56,78,90,35,45,67,79,89]
i=0
evensum=0
while i<len(number):
    if number[i]%2==0:
        evensum=evensum+number[i]
    i=i+1
print("total of evensum",evensum)        
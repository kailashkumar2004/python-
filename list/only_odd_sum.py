number=[11,24,34,56,78,90,35,45,67,79,89]
i=0
oddsum=0
while i<len(number):
    if number[i]%2!=0:
        oddsum =oddsum +number[i]
    i=i+1
print("total of oddsum",oddsum) 


list=[11,21,34,54,67,89,90,66,79,50,97,65,42,10]
i=0
oddsum=0
while i<len(list):
    if list[i]%2!=0:
        oddsum=oddsum+list[i]
    i=i+1
print("total of oddsum",oddsum)        
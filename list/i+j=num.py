list = [10, 20, 15, 15, 29, 69, 50, 12, 18, 16, 14, 50, 70, 80, 90]
output = []
num = 30

for i in list:
    for j in list:
        if i + j == num:
            output.append([i, j])

print(output)


number=[20,15,20,25,30,10,78,90,54,63,12,28]
output=[]
num=40
for i in number:
    for j in number:
      if  i+j==num:
            output.append([i,j])
print(output)            
def number():
    list=[12,18,20,10,49,80,76,5,15,15,16,14,13,17]
    num=30
    output=[]
    for i in list:
        for j in list:
            if i+j==num:
                output.append([i,j])
    print(output)
number()                
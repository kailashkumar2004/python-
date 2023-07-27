def num():
    list=[90,76,54,32,87,100,36]
    max=list[0]
    i=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    print(max)
num()
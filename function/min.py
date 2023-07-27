def num():
    list=[2,5,7,9,65,34,57,90,21,22,32,43,54,36]
    min=list[0]
    i=0
    while i<len(list):
        if list[i]<min:
            min=list[i]
        i=i+1
    print(min) 
num() 
def num():
    list=[1,2,3,4,5,6,7,8,9,11,21,32,34,56,76,87,98,89,90,76,1,3,2,4,5,6,7,8,9,11] 
    uniqueNumber=[]
    for number in list:
        if number not in uniqueNumber:
            uniqueNumber.append(number) 
    print(uniqueNumber)
num() 
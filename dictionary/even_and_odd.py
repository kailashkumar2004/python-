num = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8"}

for i in num:
    if int(num[i]) % 2 == 0:
        print(num[i], "is even")
    else:
        print(num[i], "is odd")  
          
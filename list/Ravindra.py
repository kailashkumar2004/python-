number = [12, 13, 14, 16]
output = []
i = 0

while i < len(number):
    j = 1
    while j < len(number):
        output.append(number[i:j+1])
        j = j + 1
    i = i + 1

print("Output:", output)
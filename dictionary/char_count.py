name="kailashkumar"
charcount={}
for char in name:
    charcount[char] = charcount.get(char, 0) + 1

print(charcount)
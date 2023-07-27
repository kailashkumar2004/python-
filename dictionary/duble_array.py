num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

obj = {k: v for k, v in zip(keys, num)}
print(obj)

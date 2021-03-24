string = input("")
words = string.split(" ")
words = [w for w in words if w !=""]
print(len(words))

n = int(input())
result = 0
for _ in range(n):
    word = input()
    res = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) >0:
                res += 1
    if res == 0:
        result += 1
print(result)        

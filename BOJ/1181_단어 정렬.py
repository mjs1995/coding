word = list()
sorted_word = list()

for _ in range(int(input())):
    word.append(input())
    
set_word = set(word)

for w in set_word:
    sorted_word.append((len(w),w))
sorted_word.sort()
for i,j in sorted_word:
    print(j)

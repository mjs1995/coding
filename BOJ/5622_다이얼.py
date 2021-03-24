alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for alp in alpabet_list:
    for i in alp:
        for x in word:
            if i == x:
                time += alpabet_list.index(alp) + 3
print(time)

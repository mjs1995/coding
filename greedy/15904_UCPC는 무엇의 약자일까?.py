sentence = input()

def find(sentence,f):
    if f in sentence:
        return sentence.index(f)
    return -1

chek_list = ['U','C','P','C']
check = True

for i in range(len(chek_list)):
    idx = find(sentence, chek_list[i])
    if idx != -1:
        sentence = sentence[idx+1:]
    else:
        check = False
        break
if check == True:
    print("I love UCPC")
else:
    print("I hate UCPC")

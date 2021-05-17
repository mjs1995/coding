def solution(s):
    new_list = s.split(' ')
    a = []
    for i in new_list:
        s= ''
        for j in range(0, len(i)):
            s+= i[j].upper() if j%2 ==0 else i[j].lower()
        a.append(s)
    return ' '.join(a)

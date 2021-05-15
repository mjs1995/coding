def solution(a, b):
     res = []
    for i in range(len(a)):
        res.append(a[i] *b[i])
    return sum(res)

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    c = 0
    for i,j in zip(A,B):
        c += i*j
    return c

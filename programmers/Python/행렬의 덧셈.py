def solution(arr1, arr2):
    tmp = []
    answer = []
    for a,b in zip(arr1,arr2):
        for c,d in zip(a,b):
            tmp.append(c+d)
        answer.append(tmp)
        tmp = []
    return answer

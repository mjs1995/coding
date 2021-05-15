def solution(absolutes, signs):
    res = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            res.append(absolutes[i])
        else:
            res.append(-absolutes[i])
    return sum(res)

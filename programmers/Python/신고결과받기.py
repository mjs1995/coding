from collections import Counter, defaultdict
def solution(id_list, report, k):
    res = []
    ans = []
    re = [] 
    dic = defaultdict(list)
    report = list(set(report))
    for i in range(len(report)):
        res.append(report[i].split(' ')[1])
    for i in range(len(Counter(res))):
        if Counter(res).most_common()[i][1] >= k:
            ans.append(Counter(res).most_common()[i][0])
    for i in range(len(report)):
        dic[report[i].split(' ')[0]].append(report[i].split(' ')[1])
    for i in id_list:
        answer = 0
        for j in range(len(dic[i])):
            for k in ans:
                if dic[i][j] == k:
                    answer += 1
        re.append(answer)            
    return re

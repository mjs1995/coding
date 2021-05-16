from itertools import combinations
def solution(numbers):
    res = set()
    for i in list(combinations(numbers,2)):
        res.add(sum(i))
    return sorted(res)
    

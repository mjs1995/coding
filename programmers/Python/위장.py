from collections import Counter

def solution(clothes):
    answer = 1
    kind = []
    
    for a, b in clothes:
        kind.append(b)
        
    kind = Counter(kind)
    
    for i in kind.values():
    	answer *= (i + 1)
    
    return answer - 1

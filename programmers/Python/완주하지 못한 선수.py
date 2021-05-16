def solution(participant, completion):
    res = []
    participant.sort()
    completion.sort()
    
    for j,k in zip(participant,completion):
        if j != k:
            return j
    return participant.pop()

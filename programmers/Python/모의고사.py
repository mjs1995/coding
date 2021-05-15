def solution(answers):
    answer = []
    answer_temp = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            cnt1 += 1
        if answers[i] == b[i%len(b)]:
            cnt2 += 1
        if answers[i] == c[i%len(c)]:
            cnt3 += 1
    answer_temp = [cnt1,cnt2,cnt3]
    
    for j,k in enumerate(answer_temp):
        if k == max(answer_temp):
            answer.append(j+1)
    return answer

solution(answers)
            

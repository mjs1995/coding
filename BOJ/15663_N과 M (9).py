def solve(N,M,array,answer, index):
    if len(answer) == M : 
        result.append(tuple(answer))
        return
    
    for i in range(len(array)):
        if i not in index :
            answer.append(array[i])
            index.append(i)
            solve(N,M,array,answer,index)
            answer.pop()
            index.pop()
            
result = []
N, M = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

solve(N, M, array, [], [])
sort_result = sorted(list(set(result)))

for element in sort_result:
    print(*element)

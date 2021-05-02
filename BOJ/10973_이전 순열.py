n = int(input())
seq = list(map(int,input().split()))

k = -1
for i in range(len(seq)-1):
    if seq[i] > seq[i+1]:
        k = i
        
if k == -1:
    print(-1)
else:
    for j in range(k+1,len(seq)):
        if seq[j] < seq[k]:
            m = j
            
    seq[k],seq[m] = seq[m], seq[k]
    
    tmp = seq[k+1:]
    tmp.sort(reverse= True)
    answer = seq[:k+1] + tmp
    
    for num in answer:
        print(num, end  = ' ')
    print()

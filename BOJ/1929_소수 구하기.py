m, n = map(int, input().split())
nums = {x for x in range(m, n+1) if x == 2 or x % 2 ==1} 

for odd in range(3, int(math.sqrt(n))+1, 2):  
    nums -= {i for i in range(2 * odd, n + 1, odd)}
    
for sosu in sorted(nums) :  
    if sosu > 1 :
        print(sosu)  

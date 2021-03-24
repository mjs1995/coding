t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    dis = y - x
    cnt = 0
    move = 1
    move_sum = 0
    while move_sum < dis:
        cnt +=1
        move_sum += move
        if cnt % 2 == 0:
            move +=1
    print(cnt)

for _ in range(3):
    data = list(map(int,input().split()))
    gowork = 3600 * data[0] + 60 * data[1] + data[2]
    offwork = 3600 * data[3] + 60 * data[4] + data[5]
    work = offwork - gowork
    print(work // 3600, work% 3600 //60, work % 60)

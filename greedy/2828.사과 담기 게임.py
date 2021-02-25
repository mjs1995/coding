n,m = map(int, input().split()) #스크린 크기 , 바구니 크기
j = int(input()) #사과개수

apples = [int(input()) for _ in range(j)]

size = m - 1
left = 1
right = left + size
count = 0

for apple in apples:
    if left <= apple <= right :
        continue
    if apple < left:
        count += abs(left - apple)
        left = apple
        right = apple + size
        continue
    if apple > right:
        count += abs(apple - right)
        left = apple - size
        right = apple
print(count)

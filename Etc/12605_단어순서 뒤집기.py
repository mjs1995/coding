from collections import deque

for case in range(int(input())):
    stack = deque(input().split())
    print(f"Case #{case+1}: ", end='')
    while len(stack) > 1:
        print(stack.pop(), end= ' ')
    print(stack.pop())

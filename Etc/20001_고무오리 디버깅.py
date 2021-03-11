from collections import deque

_ = input()
stack = deque()
while 1:
    s = input()
    if s == '고무오리 디버깅 끝':
        break
    if s == '문제':
        stack.append(1)
    elif stack and s == '고무오리':
        stack.pop()
    else:
        stack.append(1); stack.append(1)
print("고무오리야 사랑해" if not stack else "힝구")

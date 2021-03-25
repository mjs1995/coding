import sys
n = int(sys.stdin.readline())
numbers = [0 for _ in range(10000)]
for _ in range(n):
    numbers[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    if numbers[i] > 0:
        sys.stdout.write((str(i+1) +'\n')*numbers[i])

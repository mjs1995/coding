N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(L[i])
        solve(depth+1, i, N, M)
        out.pop()

solve(0, 0, N, M)

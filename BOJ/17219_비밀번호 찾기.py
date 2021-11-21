N, M = map(int, input().split())
dict = {}

for _ in range(N):
    site, password = map(str, input().split())
    dict[site] = password

for _ in range(M):
    site_address = input()
    print(dict[site_address])

# 시간복잡도 
import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
ndict = {}
for i in range(N):
    site, password = input().rstrip().split()
    ndict[site] = password 
for i in range(M):
    url = input().rstrip()
    print(ndict[url])

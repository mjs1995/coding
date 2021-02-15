import sys
while True:
    try:
        a,b,c=map(int,sys.stdin.readline().split())
        print( max( b-a , c-b)-1)
    except Exception as e:
        exit()

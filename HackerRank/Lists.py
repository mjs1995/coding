if __name__ == '__main__':
    N = int(input())
    li = []
    
    for i in range(N):
        ar = list(input().split(' '))
        
        if ar[0] == 'insert':
            li.insert(int(ar[1]), int(ar[2]))
        elif ar[0] == 'remove':
            li.remove(int(ar[1]))
        elif ar[0] == 'append':
            li.append(int(ar[1]))
        elif ar[0] == 'sort':
            li.sort()
        elif ar[0] == 'pop':
            li.pop()
        elif ar[0] == 'reverse':
            li.reverse()
        elif ar[0] == 'print':
            print(li)

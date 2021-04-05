if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a. append([name,score])
    # sorted(a, key = lambda x : x[1])[2]
    second = sorted(set([score for name, score in a]))[1]
    print('\n'.join(sorted([name for name, score in a if score == second])))

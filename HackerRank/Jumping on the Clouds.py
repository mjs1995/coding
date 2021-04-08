import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    res = 0
    ind = 0
    
    while ind != len(c)-1:
        if ind != len(c) -2 and c[ind+2] == 0:
            ind += 2
        else:
            ind += 1
        print(ind)
        res += 1
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
#    fptr.write(str(result) + '\n')

#    fptr.close()

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    s = -9999
    for y in range(len(arr) -2 ):
        for x in range(len(arr[0]) - 2):
            temp = arr[y][x] + arr[y][x+1] + arr[y][x+2]+\
                   arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
            if temp > s:
                s = temp
    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

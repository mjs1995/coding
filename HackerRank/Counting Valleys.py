import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    val_num = 0
    level = 0
    
    for i in range(steps):
        if path[i] == 'U':
            level = level + 1
        else:
            if level == 0:
                val_num = val_num +1
            level = level-1
    return val_num

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

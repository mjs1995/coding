import numpy
if __name__ == "__main__":
    val = numpy.polyval(list(map(float, input().split())), float(input()))
    print(val)

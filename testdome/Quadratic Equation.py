"""
Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. The function should return a tuple containing roots in any order. If the equation has only one solution, the function should return that solution as both elements of the tuple. The equation will always have at least one solution.

The roots of the quadratic equation can be found with the following formula: A quadratic equation.

For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1) as the roots of the equation 2x2 + 10x + 8 = 0 are -1 and -4.
"""
import math

def discriminat(a,b,c):
    result = (b*b) - 4 * a * c
    return result

def find_roots(a, b, c):
    result = (b*b) - 4 * a * c
    solution = [0,1]
    solution[0] = (-b + math.sqrt(discriminat(a,b,c))) // 2*a
    solution[1] = (-b - math.sqrt(discriminat(a,b,c))) // 2*a
    return solution

print(find_roots(2, 10, 8));

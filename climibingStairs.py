# since it the fibonacci we will answer pretty quickly.
from math import factorial
def climbStairs(self, n):
    res= 0
    two = n//2

    for i in range(two+1):
        t = i           # number of twos
        o = n-t*2       # number of ones
        res += factorial(t+o)/(factorial(t)*factorial(o))     # (two+one)!/ (two!*one!)
            
    return res
import math 
class Solution:
    def mySqrt(self, x: int) -> int:
        j = math.sqrt(x)
        floor_value = math.floor(j)
        return floor_value
        
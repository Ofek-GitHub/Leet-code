class Solution:
    def romanToInt(self, s: str) -> int:
        map_romans = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500, 
            "M": 1000
        }
        print(map_romans)
        num = 0
        value = 0
        for letter in s[::-1]:
            preValue = value
            value = map_romans.get(letter)
            if value <= preValue:
                if (preValue == value * 5 or preValue == value * 10):
                    num -= value
                else:
                    num += value
            else:
                num += value
        return num 

solution = Solution()
print(solution.romanToInt("XVIV"))

'''
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle applies to the number nine,
which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''
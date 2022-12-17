from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lenOfDigits = len(digits)
        num = digits[-1]
        for i in range(2, lenOfDigits + 1):
            num = num + digits[-i] * 10 **(i -1)
        
        num = num + 1 
        
        res = [int(x) for x in str(num)]
        return res
        
        
solution = Solution()
solution.plusOne([9,9,9,9,9])

        
class Solution:
    def isValid(self, s: str) -> bool:
        parenthess = {}
        for char in s:
            parenthess[char] = (parenthess.get(char,0) + 1)
        if parenthess["["] != parenthess["]"] or parenthess["("] != parenthess[")"] or parenthess["{"] != parenthess["}"]:
            return False
        else:
            return True


solution = Solution()
print(solution.isValid(("[[]]{{}}))((")))



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        while words[-1] == "":
            words.pop()
        return len(words[-1])




solution = Solution()
print(solution.lengthOfLastWord("Hello World   my name is ofekkkk "))
from typing import List


class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for index, num in enumerate(nums):
            compliment = target - num

            if compliment in compliments:
                return [compliments[compliment], index]
            compliments[num] = index
            print(compliments)


solution = Solution()
print(solution.twosum([2, 3, 6, 7, 11, 15], 9))

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove((val))
        k = len(nums)
        return nums, k


solution = Solution()
print(solution.removeElement([1, 2, 4, 3, 4, 5, 5, 4, 5, 4], 4))

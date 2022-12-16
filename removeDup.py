from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        number = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] > number:
                nums[k] = nums[i]
                number = nums[i]
                k = k +1
        for j in range(k,len(nums)):
            nums[j] = "_"
        return k , nums



solution = Solution()
print(solution.removeDuplicates([0, 1, 2, 3, 3, 3, 4, 5, 5]))








from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(map(int,str(x)))
        for index,num in enumerate(lst):
            if lst[index] == lst[-1]:
                lst.pop()
            else:
                print("This is not a Palindrome")
                return
        print("This is Palindrome")
        return





solution = Solution()
solution.isPalindrome(13322331)

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_array = list(str(x))
        x_array_reverse = list(str(x))
        x_array_reverse.reverse()
        if x_array == x_array_reverse:
            return True                         also a nice solution! 
        return False
"""
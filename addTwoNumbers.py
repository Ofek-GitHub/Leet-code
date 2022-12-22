from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)    
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


solution = Solution()

# Create the first linked list
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# Create the second linked list
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

# Add the two linked lists
result = solution.addTwoNumbers(node1, node4)

# Print the values of the resulting linked list
current = result
while current:
    print(current.val, end=" ")
    current = current.next

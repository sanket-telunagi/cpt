# Solution for 61. Rotate List
# Platform: LeetCode
# Date: 2026-05-05
#

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        nums = []
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next

        temp = []
        k2 = k % len(nums)
        while k2 > 0:
            temp.append(nums[-k2])
            k2 -= 1

        for i in range(len(nums) - (k % len(nums))):
            temp.append(nums[i])

        h2 = ListNode(temp[0])
        res = h2
        for i in range(1, len(temp)):
            h2.next = ListNode(temp[i])
            h2 = h2.next
        return res

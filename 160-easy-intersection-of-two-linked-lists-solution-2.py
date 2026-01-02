

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        runner_1 = headA
        runner_2 = headB

        while runner_1 is not runner_2:
            if runner_1 is None:
                runner_1 = headB

            if runner_2 is None:
                runner_2 = headA

            runner_1 = runner_1.next
            runner_2 = runner_2.next

        return runner_1


if __name__ == '__main__':
    s = Solution()



from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow_pointer = head
        fast_pointer = head.next

        while fast_pointer:
            if fast_pointer == slow_pointer:
                return True

            if fast_pointer.next:
                fast_pointer = fast_pointer.next.next
            else:
                return False

            slow_pointer = slow_pointer.next

        return False


if __name__ == '__main__':
    s = Solution()

    print(s.hasCycle())
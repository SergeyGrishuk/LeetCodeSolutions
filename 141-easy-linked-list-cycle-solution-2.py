

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(1)
        dummy.next = head

        slow_pointer = fast_pointer = dummy

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if slow_pointer is fast_pointer: # Check for same memory address and not just equality
                return True

        return False


if __name__ == '__main__':
    s = Solution()

    print(s.hasCycle())
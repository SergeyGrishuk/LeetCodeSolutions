

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummy_1 = ListNode(1)
        dummy_2 = ListNode(2)

        dummy_1.next = headA
        dummy_2.next = headB

        dummy_1_switched = False
        dummy_2_switched = False

        while True:
            if dummy_1 is dummy_2:
                return dummy_1

            if dummy_1.next:
                dummy_1 = dummy_1.next
            else:
                if not dummy_1_switched:
                    dummy_1 = headB
                    dummy_1_switched = True
                else:
                    return None

            if dummy_2.next:
                dummy_2 = dummy_2.next
            else:
                if not dummy_2_switched:
                    dummy_2 = headA
                    dummy_2_switched = True
                else:
                    return None


if __name__ == '__main__':
    s = Solution()

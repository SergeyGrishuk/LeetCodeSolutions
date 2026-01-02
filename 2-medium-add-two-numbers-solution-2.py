

from typing import Optional

from utils import build_linked_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                            l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        head = node

        carry = 0

        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            carry = val // 10
            node.next = ListNode(val % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next

        if carry > 0:
            node.next = ListNode(carry)

        return head.next
        

def main():
    s = Solution()

    l1 = build_linked_list([8, 3, 2])
    l2 = build_linked_list([9, 2, 1])

    added_linked_list = s.addTwoNumbers(l1, l2)

    while added_linked_list:
        print(added_linked_list.val)

        added_linked_list = added_linked_list.next


main()


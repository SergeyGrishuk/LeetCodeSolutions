

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
        head = l1 if l1 else l2

        carry = False

        while l1:
            l1.val += l2.val if l2 else 0

            if carry:
                l1.val += 1
                carry = False

            if l1.val >= 10:
                l1.val -= 10
                carry = True

            if not l1.next and l2 and l2.next:
                l1.next = l2.next
                l2 = None
            elif not l1.next and carry:
                l1.next = ListNode(1)
                carry = False

            l1 = l1.next
            l2 = l2.next if l2 else None

        return head


def main():
    s = Solution()

    l1 = build_linked_list([])
    l2 = build_linked_list([1])

    added_linked_list = s.addTwoNumbers(l1, l2)

    while added_linked_list:
        print(added_linked_list.val)

        added_linked_list = added_linked_list.next


main()


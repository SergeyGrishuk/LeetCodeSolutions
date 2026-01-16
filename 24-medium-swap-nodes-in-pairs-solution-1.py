

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first

        return dummy.next


def create_linked_list(lst: list[int]) -> Optional[ListNode]:
    head = ListNode()
    current_node = head

    for i in lst:
        current_node.next = ListNode(i)
        current_node = current_node.next

    return head.next


def main():
    s = Solution()

    linked_list = create_linked_list([1, 2, 3, 4, 5])

    swapped_list = s.swapPairs(linked_list)

    while swapped_list:
        print(swapped_list.val)

        swapped_list = swapped_list.next


main()

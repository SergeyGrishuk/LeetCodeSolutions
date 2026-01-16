

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# This solution uses O(N) time and O(N) space as it create a new stack frame for each recursive function call.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next


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

    linked_list = create_linked_list([1, 2, 3])

    # while linked_list:
    #     print(linked_list.val)

    #     linked_list = linked_list.next

    modified_list = s.removeNthFromEnd(linked_list, 3)

    while modified_list:
        print(modified_list.val)

        modified_list = modified_list.next

main()

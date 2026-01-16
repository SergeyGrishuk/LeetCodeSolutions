

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# This solution uses O(N) time and O(N) space as it create a new stack frame for each recursive function call.
class Solution:
    def recurse_remove(self, node: Optional[ListNode], n: int) -> int:
        if node is None:
            return 0

        n_from_end = self.recurse_remove(node.next, n)

        if n_from_end == n:
            node.next = node.next.next

        return n_from_end + 1


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_from_end = self.recurse_remove(head, n)

        if n_from_end == n:
            return head.next

        return head


def create_linked_list(l: list[int]) -> Optional[ListNode]:
    head = ListNode()
    current_node = head

    for i in l:
        current_node.next = ListNode(i)
        current_node = current_node.next

    return head.next


def main():
    s = Solution()

    linked_list = create_linked_list([1])

    # while linked_list:
    #     print(linked_list.val)

    #     linked_list = linked_list.next

    modified_list = s.removeNthFromEnd(linked_list, 1)

    while modified_list:
        print(modified_list.val)

        modified_list = modified_list.next

main()

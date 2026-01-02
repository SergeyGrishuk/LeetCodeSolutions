

from random import randint
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node = ListNode(0, None)
        head = current_node

        while list1 and list2:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        current_node.next = list1 if list1 else list2

        return head.next


def generate_linked_list(value: int = 20, parent_node: Optional[ListNode] = None) -> ListNode:
    if value > 0:
        node = ListNode(val=value, next=parent_node)

        value -= randint(1, 3)

        return generate_linked_list(value=value, parent_node=node)

    return parent_node


if __name__ == '__main__':
    linked_list_1 = generate_linked_list()
    linked_list_2 = generate_linked_list()

    # head = linked_list_1
    #
    # while True:
    #     print(head.val)
    #
    #     if head.next:
    #         head = head.next
    #     else:
    #         break

    s = Solution()
    merged_list = s.mergeTwoLists(linked_list_1, linked_list_2)

    while True:
        print(merged_list.val)

        if merged_list.next:
            merged_list = merged_list.next
        else:
            break

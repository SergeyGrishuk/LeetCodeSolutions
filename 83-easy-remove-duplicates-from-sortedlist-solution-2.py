


from random import randint
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            current_node = head
        else:
            return head

        while current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return head


def generate_linked_list(value: int = 10, parent_node: Optional[ListNode] = None) -> ListNode:
    node = ListNode(val=value, next=parent_node)

    if randint(1, 10) % 2 == 0:
        value -= 1

    if value > 0:
        return generate_linked_list(value=value, parent_node=node)

    return node


if __name__ == '__main__':
    s = Solution()

    sorted_linked_list = generate_linked_list()
    sorted_linked_list_head = sorted_linked_list

    print("Original linked list:")

    while sorted_linked_list:
        print(sorted_linked_list.val)

        sorted_linked_list = sorted_linked_list.next

    print("Filtered linked list")

    filtered_linked_list = s.deleteDuplicates(sorted_linked_list_head)

    while filtered_linked_list:
        print(filtered_linked_list.val)

        filtered_linked_list = filtered_linked_list.next

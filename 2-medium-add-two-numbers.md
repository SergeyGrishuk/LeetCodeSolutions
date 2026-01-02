

# 2 Add Two Numbers

Difficulty: Medium
Topics: Linked Lists


## Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

```
List 1: [2] -> [4] -> [3]
List 2: [5] -> [6] -> [4]

Result: [7] -> [0] -> [8]

342 + 465 = 807
```

## Constraints:

The number of nodes in each linked list is in the range `[1, 100]`.

`0 <= Node.val <= 9`

It is guaranteed that the list represents a number that does not have leading zeros.


## Solution 1

This solution uses O(N) complexity and O(1) space. It does not create a new linked list, instead it "re-uses" the first list `l1`.

To solve the problem with different list lenghts, I "rewire" the rest of `l2` to `l1`.

In an interview, clarify that it is OK to reuse the existing list. It might be prohibited and require to create a new linked list.

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
```


## Solution 2

This solution uses a more "production" approach to the problem. It has a runtime complexity of O(N) and space of O(N).
The difference between this solution and the first is that in this solution I create a new linked list instead of modifing an existing one. This increases the memory usage from O(1) to O(N) as a new memory for the new list has to be allocated.

```py
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
```


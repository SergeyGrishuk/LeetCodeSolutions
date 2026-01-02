

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if node is None:
                continue

            if node.left is None and node.right is None:
                return depth

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return 0


def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    # Create the root
    root = TreeNode(values[0])
    queue = [root]
    i = 1

    # Use a queue to attach children level by level
    while i < len(values):
        current = queue.pop(0)

        # Assign Left Child
        if i < len(values):
            if values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

        # Assign Right Child
        if i < len(values):
            if values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

    return root


def print_tree(node: Optional[TreeNode], level: int = 0, prefix: str = "Root: "):
    if not node:
        return

    # 1. Print Right Branch (Top)
    print_tree(node.right, level + 1, "┌── ")

    # 2. Print Current Node
    # The indentation (4 spaces per level) shows the depth
    print("    " * level + prefix + str(node.val))

    # 3. Print Left Branch (Bottom)
    print_tree(node.left, level + 1, "└── ")


if __name__ == '__main__':
    s = Solution()

    tree = build_tree_from_list([3,9,20,None,None,15,7])
    print_tree(tree)

    print(s.minDepth(tree))

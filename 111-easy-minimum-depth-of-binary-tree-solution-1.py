

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        if not root:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if left_depth == 0 and right_depth > 0:
            return 1 + right_depth

        if right_depth == 0 and left_depth > 0:
            return 1 + left_depth

        return 1 + min(left_depth, right_depth)


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

    tree = build_tree_from_list([2,None,3,None,4,None,5,None,6])
    print_tree(tree)

    print(s.minDepth(tree))

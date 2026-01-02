

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _depth_diff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth_left = self._depth_diff(root.left)
        depth_right = self._depth_diff(root.right)

        if depth_left == -1 or depth_right == -1:
            return -1

        return -1 if abs(depth_left - depth_right) > 1 else 1 + max(depth_left, depth_right)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self._depth_diff(root) != -1


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

# --- Example Usage ---
# tree = build_tree_from_list([1, 2, 2, 3, 3, None, None, 4, 4])
# print_tree(tree)


if __name__ == '__main__':
    s = Solution()

    tree = build_tree_from_list([1,2,2,3,None,None,3,4,None,None,4])
    print_tree(tree)

    print(s.isBalanced(tree))

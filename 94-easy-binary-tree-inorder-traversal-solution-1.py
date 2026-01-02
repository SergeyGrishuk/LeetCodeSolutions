

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def func(self, node: Optional[TreeNode], l: List[int]) -> None:
        if not node:
            return

        self.func(node.left, l)

        l.append(node.val)

        if node.right:
            self.func(node.right, l)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []

        self.func(root, l)

        return l


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


if __name__ == '__main__':
    s = Solution()

    tree = build_tree_from_list([1,2,3,4,5,None,8,None,None,6,7,9])
    print(s.inorderTraversal(tree))


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _is_mirror(self, node_1: Optional[TreeNode], node_2: Optional[TreeNode]) -> bool:
        if not node_1 or not node_2:
            return node_1 == node_2

        if node_1.val != node_2.val:
            return False

        return self._is_mirror(node_1.left, node_2.right) and self._is_mirror(node_1.right, node_2.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._is_mirror(root.left, root.right) if root else False


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

    tree = build_tree_from_list([1,2,2,3,4,4,3])

    print(s.isSymmetric(tree))

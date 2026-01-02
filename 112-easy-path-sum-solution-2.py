

from typing import Optional

from utils import build_tree_from_list, print_tree


null = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return targetSum - root.val == 0

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


if __name__ == '__main__':
    s = Solution()

    tree = build_tree_from_list([5,4,8,11,null,13,4,7,2,null,null,null,1])
    print_tree(tree)

    print(s.hasPathSum(tree, 22))

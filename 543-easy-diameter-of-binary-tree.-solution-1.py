

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_diameter: int = 0


    def get_depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        depth_left = self.get_depth(node.left)
        depth_right = self.get_depth(node.right)

        if depth_left + depth_right > self.max_diameter:
            self.max_diameter = depth_left + depth_right

        return 1 + max(depth_left, depth_right)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_depth(root)

        return self.max_diameter



def main():
    s = Solution()


main()

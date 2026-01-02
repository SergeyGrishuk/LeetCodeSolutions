

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _balanced_assembler(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left == right:
            return None

        mid = (left + right) // 2

        return TreeNode(
            val=nums[mid],
            left=self._balanced_assembler(nums, left, mid),
            right=self._balanced_assembler(nums, mid + 1, right)
        )


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self._balanced_assembler(nums, 0, len(nums))


if __name__ == '__main__':
    s = Solution()

    s.sortedArrayToBST([-10, -3, 0, 5, 9])
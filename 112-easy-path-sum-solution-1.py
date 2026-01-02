

from typing import Optional
from collections import deque

import utils
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
        queue = deque([(root, 0)])

        while queue:
            node, sum = queue.popleft() # BFS
            print(f"Sum: {sum}")
            if node is None:
                continue

            if node.left is None and node.right is None:
                if sum + node.val == targetSum:
                    return True

            queue.append((node.left, sum + node.val))
            queue.append((node.right, sum + node.val))

        return False



if __name__ == '__main__':
    s = Solution()

    tree = utils.build_tree_from_list([5,4,8,11,null,13,4,7,2,null,null,null,1])
    print_tree(tree)

    print(s.hasPathSum(tree, 22))

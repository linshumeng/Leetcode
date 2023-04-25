from typing import *
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([root])
        res = deque([root.val])
        while queue:
            node = queue.popleft()
            path_sum = res.popleft()
            if not node.left and not node.right and path_sum == targetSum:
                return True
            if node.left:
                queue.append(node.left)
                res.append(path_sum + node.left.val)
            if node.right:
                queue.append(node.right)
                res.append(path_sum + node.right.val)
        return False

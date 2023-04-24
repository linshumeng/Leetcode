from typing import *
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left and not node.left.left and not node.left.right:
                    res += node.left.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

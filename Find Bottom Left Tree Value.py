from typing import *
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                if i == 0:
                    res = queue[0].val
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

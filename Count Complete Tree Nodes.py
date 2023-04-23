from typing import *
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                res += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

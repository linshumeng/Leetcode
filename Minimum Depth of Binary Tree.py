from typing import *
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        que = [(root, 1)]
        while que:
            node, height = que.pop(0)
            if node.left is None and node.right is None:
                return height
            if node.left:
                que.append((node.left, height + 1))
            if node.right:
                que.append((node.right, height + 1))

from typing import *
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res
        queue = deque([root])
        path_ = deque([str(root.val)])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                path = path_.popleft()
                if not(node.left or node.right):
                    res.append(path)
                if node.left:
                    queue.append(node.left)
                    path_.append(path + '->' + str(node.left.val))
                if node.right:
                    queue.append(node.right)
                    path_.append(path + '->' + str(node.right.val))
        return res

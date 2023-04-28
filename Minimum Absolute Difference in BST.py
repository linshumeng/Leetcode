from typing import *
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder_list = []

        def inordertraversal(root):
            if not root:
                return
            inordertraversal(root.left)
            inorder_list.append(root.val)
            inordertraversal(root.right)

        inordertraversal(root)
        res = float("inf")
        for i in range(1, len(inorder_list)):
            res = min(res, abs(inorder_list[i] - inorder_list[i - 1]))
        return res

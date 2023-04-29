from typing import *
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left and root.right:
                root = root.right
                return root
            if root.left and not root.right:
                root = root.left
                return root
            else:
                v = root.right
                while v.left:
                    v = v.left
                v.left = root.left
                root = root.right
                return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

from typing import *
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res_dict = {}
        res_list = []

        def inordertraversal(root):
            if not root:
                return
            inordertraversal(root.left)
            if root.val in res_dict:
                res_dict[root.val] += 1
            else:
                res_dict[root.val] = 1
            inordertraversal(root.right)

        inordertraversal(root)
        max_value = max(res_dict.values())
        for key, value in res_dict.items():
            if value == max_value:
                res_list.append(key)
        return res_list

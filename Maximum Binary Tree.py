from typing import *
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        root_val = max(nums)
        root_index = nums.index(root_val)
        nums_left = nums[:root_index]
        nums_right = nums[root_index + 1:]
        root = TreeNode(root_val)
        root.left = self.constructMaximumBinaryTree(nums_left)
        root.right = self.constructMaximumBinaryTree(nums_right)
        return root

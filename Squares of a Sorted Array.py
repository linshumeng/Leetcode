from typing import *


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            # print(nums[left]**2, nums[right]**2)
            if nums[left]**2 < nums[right]**2:
                res[i] = nums[right]**2
                right -= 1
            else:
                res[i] = nums[left]**2
                left += 1
            # print(res)
        return res


sol = Solution()
nums = [-4, -1, 0, 3, 10]
print(sol.sortedSquares(nums))

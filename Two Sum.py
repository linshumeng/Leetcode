from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        size = len(nums)
        for i in range(size):
            residual = target - nums[i]
            if residual in dic:
                return [i, dic[residual]]
            else:
                dic[nums[i]] = i
            print(nums[i], residual, dic)


sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))

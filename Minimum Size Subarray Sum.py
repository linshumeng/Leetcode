from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sum = 0
        index = 0
        for i in range(len(nums) - 1):
            sum += nums[i]
            while sum >= target:
                res = min(res, i - index + 1)
                sum -= nums[index]
                index += 1

        if res == float("inf"):
            return 0
        else:
            return res


sol = Solution()
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(sol.minSubArrayLen(target, nums))

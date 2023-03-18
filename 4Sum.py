from typing import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]:
                    continue
                p, q = k + 1, n - 1
                while p < q:
                    cur = nums[i] + nums[k] + nums[p] + nums[q]
                    if cur > target:
                        q -= 1
                    elif cur < target:
                        p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        while p + 1 < q and nums[p] == nums[p + 1]:
                            p += 1
                        while q - 1 > p and nums[q] == nums[q - 1]:
                            q -= 1
                        p += 1
                        q -= 1
        return res

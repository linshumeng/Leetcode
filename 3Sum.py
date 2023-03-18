from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                j, k = i + 1, n - 1
                while j < k:
                    cur = nums[i] + nums[j] + nums[k]
                    if cur > 0:
                        k -= 1
                    elif cur < 0:
                        j += 1
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        while j + 1 < k and nums[j] == nums[j + 1]:
                            j += 1
                        while k - 1 > j and nums[k] == nums[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
        return res

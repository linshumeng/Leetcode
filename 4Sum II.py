from typing import *


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = {}
        for i in nums1:
            for j in nums2:
                if i + j in dic:
                    dic[i + j] += 1
                else:
                    dic[i + j] = 1
        print(dic)
        count = 0
        for k in nums3:
            for l in nums4:
                if -k - l in dic:
                    count += dic[-k - l]
        return count

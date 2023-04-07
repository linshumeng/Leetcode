from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        value_list = list(nums_dict.values())
        value_list.sort(reverse=True)
        value_list = value_list[:k]
        res = []
        for i in value_list:
            for j in nums_dict.keys():
                if nums_dict[j] == i and j not in res:
                    res.append(j)
        return res

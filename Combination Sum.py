from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(candidates, target, sum, StartIndex):
            if sum == target:
                res.append(path[:])
                return
            if sum > target:
                return
            for i in range(StartIndex, len(candidates)):
                path.append(candidates[i])
                sum += candidates[i]
                backtrack(candidates, target, sum, i)
                sum -= candidates[i]
                path.pop()

        backtrack(candidates, target, 0, 0)
        return res

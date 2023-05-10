from typing import *


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(n, k, StartIndex, sum):
            if len(path) == k and sum == n:
                res.append(path[:])
                return
            for i in range(StartIndex, 10):
                sum += i
                path.append(i)
                backtrack(n, k, i + 1, sum)
                sum -= i
                path.pop()

        backtrack(n, k, 1, 0)
        return res

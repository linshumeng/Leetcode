from typing import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loops = n // 2
        mid = n // 2
        count = 1

        for loop in range(0, loops):
            for i in range(starty, n - loop - 1):
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - loop - 1):
                nums[i][n - loop - 1] = count
                count += 1
            for i in range(n - loop - 1, starty, -1):
                nums[n - loop - 1][i] = count
                count += 1
            for i in range(n - loop - 1, startx, -1):
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1

        if n % 2 != 0:
            nums[mid][mid] = n**2
        return nums


sol = Solution()
n = 3
print(sol.generateMatrix(n))

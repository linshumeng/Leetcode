from typing import *


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        res = ""
        while i < len(s):
            reverse = s[i: i + k]
            res = res + reverse[::-1] + s[i + k: i + 2 * k]
            i += 2 * k
        return res

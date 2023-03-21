from typing import * 


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return " ".join(s)

from typing import *

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        begin = needle[0]
        l = len(needle)
        if len(haystack) < l:
            return -1
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == begin:
                if haystack[i: i+l] == needle:
                    return i
        return -1
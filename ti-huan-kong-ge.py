from typing import *


class Solution:
    def replaceSpace(self, s: str) -> str:
        count = s.count(' ')
        res = list(s)
        res.extend([' '] * count * 2)
        pointer_s, pointer_res = len(s)-1, len(res)-1
        while pointer_s >= 0:
            if s[pointer_s] != ' ':
                res[pointer_res] =  s[pointer_s]
                pointer_res -= 1
            else:
                res[pointer_res-2: pointer_res+1] = '%20'
                pointer_res -=3
            pointer_s -= 1

        return ''.join(res)

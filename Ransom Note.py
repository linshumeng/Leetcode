from typing import *


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dic = {}
        for i in magazine:
            if i in magazine_dic:
                magazine_dic[i] += 1
            else:
                magazine_dic[i] = 1
        print(magazine_dic)

        for j in ransomNote:
            if j in magazine_dic:
                magazine_dic[j] -= 1
                if magazine_dic[j] < 0:
                    return False
            else:
                return False
        return True

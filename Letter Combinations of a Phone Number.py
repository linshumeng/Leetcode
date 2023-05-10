from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"], }

        res = []

        def backtrack(comb, index):
            if len(comb) == len(digits):
                res.append(comb)
                return
            for letter in letter_map[digits[index]]:
                backtrack(comb + letter, index + 1)

        if len(digits) == 0:
            return []
        backtrack("", 0)
        return res

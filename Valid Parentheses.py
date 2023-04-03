from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or stack[-1] != i:
                return False
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False

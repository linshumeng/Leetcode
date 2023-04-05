from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(i)
            else:
                first = stack.pop()
                second = stack.pop()
                res = int(eval(f'{second} {i} {first}'))
                stack.append(res)
        return int(stack.pop())

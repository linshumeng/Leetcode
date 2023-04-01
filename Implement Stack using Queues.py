from typing import *
from collections import deque


class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            # using popleft() will reduce time complexity
            print('que', self.que)
            return self.que.pop()

    def top(self) -> int:
        if self.empty():
            return None
        else:
            return self.que[-1]

    def empty(self) -> bool:
        return not self.que

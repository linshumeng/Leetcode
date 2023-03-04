from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        cur = dummy
        while cur and cur.next and cur.next.next:
            f = cur
            s = cur.next
            t = cur.next.next

            f.next = t
            s.next = t.next
            t.next = s

            cur = cur.next.next
        return dummy.next

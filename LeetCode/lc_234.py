from collections import deque
from typing import Deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        nodes: Deque = deque()
        node = head
        while node is not None:
            nodes.append(node.val)
            node = node.next

        while len(nodes) > 1:
            if nodes.popleft() != nodes.pop():
                return False
        return True

        # if head.next is None:
        #     return False
        #
        # nodes : Deque = deque()
        # while True:
        #     nodes.append(head.val)
        #     head = head.next
        #     if head.next is None:
        #         nodes.append(head.val)
        #         break
        #
        # while len(nodes) > 1:
        #     if nodes.popleft() != nodes.pop():
        #         return False
        # return True
sol = Solution()
sol.isPalindrome()
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverse_list(l1))
        b = self.toList(self.reverse_list(l2))

        result_str = int(''.join(str(e) for e in a)) + \
                     int(''.join(str(e) for e in b))
        return self.toReversedLinkedList(str(result_str))

    # 연결 리스트 뒤집기
    def reverse_list(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list : List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # [1, 2, 3]
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

        # head = l1
        # carry = 0
        # while l1:
        #     # 캐리가 생기는 경우
        #     if l1.val + l2.val + carry > 9:
        #         l1.val = l1.val + l2.val + carry - 10
        #         carry = 1
        #     # 캐리가 생기지 않는 경우
        #     else:
        #         l1.val = l1.val + l2.val + carry
        #         carry = 0
        #
        #     if carry and not l1.next:
        #         l1.next, l2.next = ListNode(1), ListNode()
        #         carry = 0
        #     l1, l2 = l1.next, l2.next
        #
        # return head

example = ListNode(1)
head = example
example.next = ListNode(2)
example = example.next
example.next = ListNode(3)

example2 = ListNode(1)
head2 = example2
example2.next = ListNode(2)
example2 = example2.next
example2.next = ListNode(3)

sol = Solution()
sol.addTwoNumbers(head, head2)

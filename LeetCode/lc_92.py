# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # second book

        # 예외처리
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        # start, end 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next

        # first me
#         if not head or m == n:
#             return head

#         root = head

#         i = 1
#         if m == 1:
#             start = head

#         while head:
#             if i + 1 == m:
#                 start = head.next
#                 prev = head
#             if i == n:
#                 end = head
#             head = head.next
#             i += 1

#         if m == 1:
#             root = self.reverse_node(start, end, end.next)
#         else:
#             prev.next = self.reverse_node(start, end, end.next)

#         return root

#     def reverse_node(self, head: ListNode, tail: ListNode, remain: ListNode) -> ListNode:
#         rev = remain
#         while head and head != remain:
#             rev, rev.next, head = head, rev, head.next

#         return rev


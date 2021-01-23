# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # second
        # 예외처리
        if head is None:
            return head

        odd = head
        even = even_root = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_root
        return head

        # first (me)
#         if not head:
#             return head
#         odd = head
#         even_root = even = ListNode(None)
#         while odd.next:
#             p = odd.next
#             if p.next is None:
#                 even.next = p
#                 break
#             odd.next = p.next
#             even.next = p

#             even = even.next
#             odd = p.next

#         if not odd.next:
#             even.next = None

#         odd.next = even_root.next
#         return head
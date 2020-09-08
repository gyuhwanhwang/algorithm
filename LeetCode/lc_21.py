# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1에 항상 작은 값이 오도록
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

        """
        if not l1 and not l2:
            return None
        result = ListNode()
        start = result
        while l1 and l2:
            if l1.val <= l2.val: # l1 이 작거나 같을 때
                result.val = l1.val
                result.next = ListNode()
                l1 = l1.next
                result = result.next
            else:  # l2가 작을 때
                result.val = l2.val
                result.next = ListNode()
                l2 = l2.next
                result = result.next

        # l1이 남았음
        while l1:
            result.val = l1.val
            l1 = l1.next
            if l1:
                result.next = ListNode()
                result = result.next
        # l2 남았음
        while l2:
            result.val = l2.val
            l2 = l2.next
            if l2:
                result.next = ListNode()
                result = result.next
        return start
        """
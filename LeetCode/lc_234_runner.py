class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:    # 노드  수가 홀수 일경우 가운데 무시
            slow = slow.next

        # 팰린드롬 비교
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev

sol = Solution()
sol.isPalindrome()
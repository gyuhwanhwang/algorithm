# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 재귀 함수
        def reverse(node: ListNode, prev: ListNode = None):
            # node에 끝에 다다르면 이전까지 연결한 prev를 반환
            if not node:
                return prev
            # next는 현재 노드를 제외한 다음 노드, 현재 노드에는 이전까지 연결한 노드 이어줌
            next, node.next = node.next, prev
            # 노드 한칸 앞으로 전진, 이전까지 연결한것은 prev로 넘겨줌
            return reverse(next, node)
        
        return reverse(head)

        # 반복 구조
        # node는 현재, prev는 뒤집은 노드
        node, prev = head, None

        while node: # 현재 노드가 끝이 아니면
            # next는 다음 노드를 가리키고, 현재 노드의 다음은 이전까지 뒤집은거 연결
            next, node.next = node.next, prev
            # 뒤집은 노드를 prev로, 현재 노드를 next로 
            prev, node = node, next

        # 현재 노드가 끝까지 가면 뒤집혀진 연결리스트 prev 반환
        return prev
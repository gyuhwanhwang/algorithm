# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # second

        root = result = ListNode(None)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        print(heap)

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            result = result.next

            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

        # first
#         heap = []
#         for node in lists:
#             while node:
#                 heap.append(node.val)
#                 node = node.next

#         heap.sort()
#         root = node = ListNode(None)
#         for h in heap:
#             print(h)
#             node.next = ListNode(h)
#             node = node.next

#         return root.next
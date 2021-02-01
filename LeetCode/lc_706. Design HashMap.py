class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.table[index].val is None:
            self.table[index] = ListNode(key, value)
            return
        else:
            node = self.table[index]
            while node:
                # 키가 같으면 갱신
                if node.key == key:
                    node.val = value
                    return
                if node.next is None:
                    break
                node = node.next
            node.next = ListNode(key, value)
            return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.table[index].val is None:
            return -1
        node = self.table[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

        if index in self.table:
            node = self.table[index]
            while node:
                if node.key == key:
                    return node.val
                node = node.next
        else:
            return -1

    #     def remove(self, key: int) -> None:
    #         """
    #         Removes the mapping of the specified value key if this map contains a mapping for the key
    #         """
    #         index = key % self.size
    #         if self.table[index].val is None:
    #             return

    #         node = self.table[index]
    #         root = prev = ListNode(None)
    #         prev.next = node
    #         while node:
    #             if node.key == key:
    #                 prev.next = node.next
    #                 if root.next is None:
    #                     self.table[index] = ListNode()
    #                 else:
    #                     self.table[index] = root.next
    #                 return
    #             node = node.next
    #             prev = prev.next
    #         return

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].val is None:
            return

        node = self.table[index]
        if node.key == key:
            self.table[index] = ListNode() if node.next is None else node.next
            return

        prev = node
        while node:
            if node.key == key:
                prev.next = node.next
                return
            prev, node = node, node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
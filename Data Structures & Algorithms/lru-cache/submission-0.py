class LRUCache:
    class Node:
        def __init__(self, key: int, val: int, prev: Node | None = None, next: Node | None = None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.current_size = 0
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev

    def _add_to_tail(self, n):
        n.prev = self.tail.prev
        n.next = self.tail
        self.tail.prev.next = n
        self.tail.prev = n

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        n = self.m[key]
        self._remove(n)
        self._add_to_tail(n)
        return n.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            n = self.m[key]
            n.val = value
            self._remove(n)
            self._add_to_tail(n)
        else:
            if len(self.m) == self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.m[lru.key]
            n = self.Node(key, value)
            self._add_to_tail(n)
            self.m[key] = n
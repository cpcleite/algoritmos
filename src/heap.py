from DoublyLinkedList import DLinkedList


class HeapMin():
    def __init__(self):
        self.keys = DLinkedList()

    def insert(self, new):
        pos = self.keys.size

        self.keys.addLast(new)

        # Bubble up
        parent = pos // 2
        while (pos > 0) and (self.keys[pos] < self.keys[parent]):
            self.keys[pos], self.keys[parent] = self.keys[parent], self.keys[pos]
            pos = parent
            parent = pos // 2


h = HeapMin()
h.insert(4)
h.insert(4)
h.insert(8)
h.insert(9)
h.insert(4)
h.insert(12)
h.insert(9)
h.insert(11)
h.insert(13)
h.insert(7)
h.insert(10)
h.insert(5)

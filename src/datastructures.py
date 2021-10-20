class Node():
    """
    Represents linked list node containing data.
    """

    def __init__(self, item, prev, next):
        self.prev = prev
        self.next = next
        self.item = item

    def __repr__(self):
        return str(self.item)


class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.iter = None

    def clear(self):
        """
        Clear the linked list.
        """
        trav = self.head
        while trav is not None:
            next = trav.next
            trav.prev = None
            trav.next = None
            trav.item = None
            trav = next

        trav = None
        self.size = 0
        self.head = None
        self.tail = None

    def size(self):
        """
        Return the number of nodes in the list.
        """
        return self.size

    def isEmpty(self):
        """
        Tests if list is empty.
        """
        return self.size == 0

    def addLast(self, item):
        """
        Adds an item to the end of the list.
        """
        if self.isEmpty():
            self.tail = Node(item, None, None)
            self.head = self.tail
        else:
            self.tail.next = Node(item, self.tail, None)
            self.tail = self.tail.next

        self.size += 1

    def addFirst(self, item):
        """
        Adds an item to the beginning of the list.
        """
        if self.isEmpty():
            self.head = Node(item, None, None)
            self.tail = self.head
        else:
            self.head.prev = Node(item, None, self.head)
            self.head = self.head.prev

        self.size += 1

    def add(self, item):
        self.addLast(item)

    def addAt(self, index, item):
        """
        Adds an item at index position.
        """
        if index <= 0:
            self.addFirst(item)

        elif index >= self.size:
            self.addLast(item)

        else:
            # Moves to the required position
            aux = self.head
            for i in range(0, index-1):
                aux = aux.next

            # Insert Node
            inserted = Node(item, aux, aux.next)
            aux.next.prev = inserted
            aux.next = inserted

            self.size += 1

    def removeFirst(self):
        """
        Removes first list item.
        """
        if self.isEmpty():
            return None

        else:
            item = self.head.item
            self.head.item = None
            self.head.prev = None
            self.size -= 1

            if self.size == 0:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

            return item

    def removeLast(self):
        """
        Removes last list item.
        """
        if self.isEmpty():
            return None

        else:
            item = self.tail.item
            self.tail.item = None
            self.tail.next = None
            self.size -= 1

            if self.size == 0:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

            return item

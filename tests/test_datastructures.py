"""
Tests datastructures objects.

Created on Tue Oct 19 17:17

@author: Celso Leite
"""
from src.datastructures import LinkedList, Node


def test_Node__init__():
    """
    Tests Node Creation consistency.
    """
    x = Node(1, None, None)
    z = Node(3, None, x)
    y = Node(2, x, z)

    assert x.item == 1
    assert y.item == 2
    assert z.item == 3
    assert y.prev.item == 1
    assert y.next.item == 3
    assert z.prev == None
    assert y.prev == x
    assert y.next == z


def test_LinkedList__init__():
    # Empty Linked List
    llist = LinkedList()

    assert llist.size == 0
    assert llist.isEmpty()


def test_LinkedList_add():
    llist = LinkedList()

    # Tests item addition
    llist.add(0)

    assert llist.size == 1
    assert llist.head.item == 0
    assert llist.tail.item == 0
    assert llist.tail == llist.head
    assert llist.head.next is None
    assert llist.tail.prev is None

    llist.add(1)
    assert llist.size == 2
    assert llist.head.item == 0
    assert llist.tail.item == 1
    assert llist.head.next == llist.tail
    assert llist.head.prev is None
    assert llist.tail.prev == llist.head
    assert llist.tail.next is None

    llist.add(2)
    assert llist.size == 3
    assert llist.head.item == 0
    assert llist.tail.item == 2
    assert llist.head.next.item == 1
    assert llist.head.prev is None
    assert llist.tail.next is None
    assert llist.tail.prev.item == 1


def test_LinkedList_addFirst():
    """
    Tests addFirst LinkedList routine
    """
    llist = LinkedList()

    # Tests item addition
    llist.addFirst(0)

    assert llist.size == 1
    assert llist.head.item == 0
    assert llist.tail.item == 0
    assert llist.tail == llist.head
    assert llist.head.next is None
    assert llist.tail.prev is None

    llist.addFirst(1)
    assert llist.size == 2
    assert llist.head.item == 1
    assert llist.tail.item == 0
    assert llist.head.next == llist.tail
    assert llist.head.prev is None
    assert llist.tail.prev == llist.head
    assert llist.tail.next is None

    llist.addFirst(2)
    assert llist.size == 3
    assert llist.head.item == 2
    assert llist.tail.item == 0
    assert llist.head.next.item == 1
    assert llist.head.prev is None
    assert llist.tail.next is None
    assert llist.tail.prev.item == 1


def test_LinkedList_addLast():
    """
    Tests addLast LinkedList routine
    """
    llist = LinkedList()

    # Tests item addition
    llist.addLast(0)

    assert llist.size == 1
    assert llist.head.item == 0
    assert llist.tail.item == 0
    assert llist.tail == llist.head
    assert llist.head.next is None
    assert llist.tail.prev is None

    llist.addLast(1)
    assert llist.size == 2
    assert llist.head.item == 0
    assert llist.tail.item == 1
    assert llist.head.next == llist.tail
    assert llist.head.prev is None
    assert llist.tail.prev == llist.head
    assert llist.tail.next is None

    llist.addLast(2)
    assert llist.size == 3
    assert llist.head.item == 0
    assert llist.tail.item == 2
    assert llist.head.next.item == 1
    assert llist.head.prev is None
    assert llist.tail.next is None
    assert llist.tail.prev.item == 1


def test_LinkedList_addAt():
    llist = LinkedList()

    llist.add(0)
    llist.add(1)
    llist.add(2)
    llist.add(3)

    # Insertion at a position
    llist.addAt(2, '+')
    assert llist.size == 5
    assert llist.head.next.next.item == '+'


def test_LinkedList_clear():
    # Prepare list
    llist = LinkedList()
    llist.add(0)
    llist.add(1)
    llist.add('+')
    llist.add(2)
    llist.add(3)

    assert llist.size == 5
    assert llist.head.next.next.item == '+'
    assert llist.head.item == 0
    assert llist.tail.item == 3

    # Test clear
    llist.clear()
    assert llist.isEmpty()
    assert llist.size == 0
    assert llist.head is None
    assert llist.tail is None


def test_LinkedList_removeFisrt():

    llist = LinkedList()
    llist.add(0)
    llist.add(1)
    llist.add('+')
    llist.add(2)
    llist.add(3)

    assert llist.size == 5
    assert llist.head.next.next.item == '+'
    assert llist.head.item == 0
    assert llist.tail.item == 3

    # Remove First
    assert llist.removeFirst() == 0
    assert llist.head.item == 1
    assert llist.head.prev is None
    assert llist.head.next.item == '+'
    assert llist.size == 4

    assert llist.removeFirst() == 1
    assert llist.head.item == '+'
    assert llist.head.prev is None
    assert llist.head.next.item == 2
    assert llist.size == 3

    assert llist.removeFirst() == '+'
    assert llist.head.item == 2
    assert llist.head.prev is None
    assert llist.head.next.item == 3
    assert llist.size == 2

    assert llist.removeFirst() == 2
    assert llist.head.item == 3
    assert llist.head.prev is None
    assert llist.head.next is None
    assert llist.size == 1

    assert llist.removeFirst() == 3
    assert llist.head is None
    assert llist.tail is None
    assert llist.isEmpty()
    assert llist.size == 0

    assert llist.removeFirst() is None


def test_LinkedList_removeLast():

    llist = LinkedList()
    llist.add(0)
    llist.add(1)
    llist.add('+')
    llist.add(2)
    llist.add(3)

    assert llist.size == 5
    assert llist.head.next.next.item == '+'
    assert llist.head.item == 0
    assert llist.tail.item == 3

    # Remove Last
    assert llist.removeLast() == 3
    assert llist.head.item == 0
    assert llist.tail.item == 2
    assert llist.tail.prev.item == '+'
    assert llist.tail.next is None
    assert llist.size == 4

    assert llist.removeLast() == 2
    assert llist.head.item == 0
    assert llist.tail.item == '+'
    assert llist.tail.prev.item == 1
    assert llist.tail.next is None
    assert llist.size == 3

    assert llist.removeLast() == '+'
    assert llist.head.item == 0
    assert llist.tail.item == 1
    assert llist.tail.prev.item == 0
    assert llist.tail.next is None
    assert llist.size == 2

    assert llist.removeLast() == 1
    assert llist.head.item == 0
    assert llist.tail.item == 0
    assert llist.tail.prev is None
    assert llist.tail.next is None
    assert llist.head.next is None
    assert llist.size == 1

    assert llist.removeLast() == 0
    assert llist.head is None
    assert llist.tail is None
    assert llist.size == 0
    assert llist.isEmpty()

    assert llist.removeFirst() is None

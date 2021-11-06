class Node():
    def __init__(self, value, left=None, right=None, prev=None):
        self.value = value
        self.left = left
        self.right = right
        self.prev = prev

    def __repr__(self) -> str:
        return str(self.value)


class BinaryTree():
    def __init__(self):
        self.root = None
        self.length = 0

    def search(self, value, node=None):
        if node == None:
            node = self.root

        if node is None:
            return False

        if value == node.value:
            return node

        elif value < node.value:
            return self.search(value, node.left)

        else:
            return self.search(value, node.right)

    def insert(self, value, node=None):

        if self.root is None:
            self.root = Node(value)
            self.length += 1
            return self.root

        if node is None:
            node = self.root

        if value <= node.value:
            if node.left is None:
                node.left = Node(value)
                node.left.prev = node
                self.length += 1
                return node.left
            else:
                return self.insert(value, node.left)

        else:
            if node.right is None:
                node.right = Node(value)
                node.right.prev = node
                self.length += 1
                return node.right

            else:
                return self.insert(value, node.right)

    def __repr__(self, node=None):

        if node is None:
            node = self.root

        if node is None:
            return '[ ]'

        if (node.left is None) and (node.right is None):
            return str(node)
        elif (node.left is None):
            return str(node) + ', ' + self.__repr__(node.right)
        elif (node.right is None):
            return self.__repr__(node.left) + ', ' + str(node)
        else:
            return self.__repr__(node.left) + ', ' +\
                self.__repr__(node.right)


T = BinaryTree()
T.insert(4)
T.insert(5)
T.insert(1)
T.insert(3)
T.insert(2)
print(str(T.length))

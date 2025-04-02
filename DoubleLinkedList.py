class Dnode():
    def __init__(self, value: int, next=None, prev=None):
        self.value: int = value
        self.next = next
        self.prev = prev

        def __repr__(self):
            return str(self.value)


# print(b.prev.value)

class DoubleLinkedList():
    def __init__(self, head: Dnode = None, tail: Dnode = None, size: int = 0):
        self.head: Dnode = head
        self.tail: Dnode = tail
        self.size: int = 0

    def append(self, value):
        new_node = Dnode(value)
        if (self.size == 0):
            self.head = new_node  # d1
            self.tail = new_node  # d1

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def traverse(self, current_node=None, flag=True):
        if (flag):
            current_node = self.head
        if (current_node is None):
            return
        print(current_node.value)
        current_node = current_node.next
        self.traverse(current_node, False)

    def traverse_inverso(self, current_node=None, flag=True):
        if (flag):
            current_node = self.tail
        if (current_node is None):
            return
        print(current_node.value)
        current_node = current_node.prev
        self.traversen_iverso(current_node, False)


Ll = DoubleLinkedList()
Ll.append(6)
Ll.append(7)
Ll.append(8)
Ll.append(9)
Ll.traverse()
Ll.traverse_inverso()

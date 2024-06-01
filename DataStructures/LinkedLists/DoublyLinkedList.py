from NodeCreation import Node


class DNode(Node):
    __slots__ = ["prev"]

    def __init__(self, item=None, next=None, prev=None) -> None:
        super().__init__(item, next)
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = self.tail = DNode()
        self.size = 0

    def isempty(self):
        return self.head == self.tail

    def append(self, ele):
        temp = DNode(ele)
        if self.isempty():
            self.head.next = temp
            temp.prev = self.head
            self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        self.size += 1

    def insert(self, index, ele):
        if index < 0 or index > self.size:
            print("Index out of bounds")
            return
        pos = self.head
        for i in range(index):
            pos = pos.next
        temp = DNode(ele, pos.next, pos)
        if pos.next:
            pos.next.prev = temp
        pos.next = temp
        if temp.next is None:
            self.tail = temp
        self.size += 1

    def find_prev(self, data):
        pos = self.head.next
        while pos.next is not None:
            if pos.next.item == data:
                return pos
            pos = pos.next
        return None

    def find(self, ele):
        pos = self.head.next
        while pos is not None:
            if pos.item == ele:
                print(f"Item {ele} found. Pos: {pos}")
                return
            pos = pos.next
        print(f"Item {ele} not found in the list")

    def remove(self, ele):
        prev = self.find_prev(ele)
        if prev is None:
            print(f"Item {ele} not in the linked list!")
            return
        delnode = prev.next
        prev.next = delnode.next
        if delnode.next:
            delnode.next.prev = prev
        if delnode == self.tail:
            self.tail = prev
        self.size -= 1

    def reverse_display(self):
        pos = self.tail
        res = ""
        while pos != self.head:
            res += str(pos.item) + " "
            pos = pos.prev
        return res.strip()

    def __str__(self) -> str:
        res = ""
        pos = self.head.next
        while pos is not None:
            res += str(pos.item) + " "
            pos = pos.next
        return res.strip()


if __name__ == "__main__":
    dll = DoublyLinkedList()
    elements = [10, 7, 9, 18, 13, 7]
    for ele in elements:
        dll.append(ele)

    print("The Doubly Linked list after insertion:")
    print(dll)
    print()

    dll.insert(2, 15)
    print("The Doubly Linked list after inserting 15 at index 2:")
    print(dll)
    print()

    dll.insert(0, 5)
    print("The Doubly Linked list after inserting 5 at index 0:")
    print(dll)
    print()

    dll.insert(dll.size, 20)
    print("The Doubly Linked list after inserting 20 at the last index:")
    print(dll)
    print()

    dll.insert(100, 25)  # should be printing "Index out of bounds"
    print("The Doubly Linked list after attempting to insert 25 at index 100:")
    print(dll)
    print()

    print("The reversed Doubly Linked list:")
    print(dll.reverse_display())

from NodeCreation import Node


class SinglyLinkedList:
    def __init__(self) -> None:
        self.tail = self.head = Node()

    def isempty(self):
        if self.head == self.tail:
            return True
        return False

    def append(self, ele):
        temp = Node(ele)
        self.tail.next = temp
        self.tail = temp

    def display(self):
        pos = self.head.next
        res = ""
        while pos != None:
            res += str(pos.item) + " "
            pos = pos.next
        print(res)
        return

    def find(self, ele):
        pos = self.head.next
        while pos != None:
            if pos.item == ele:
                print(f"Item {ele} found. Pos: {pos}")
                return
            pos = pos.next
        return f"Item {ele} not in the linked list!"

    def insert(self, insert_pos, ele):
        pos = self.head.next
        while pos != insert_pos:
            pos = pos.next
        temp = Node(ele, pos.next)
        pos.next = temp

    def find_prev(self, data):
        pos = self.head.next
        while pos.next is not None:
            if pos.next.item == data:
                return pos
            pos = pos.next
        return -1

    def remove(self, data):
        print(f"trying to delete {data}...")
        prev = self.find_prev(data)
        if prev == -1:
            print("Item not in the linked list!")
            return
        delnode = prev.next
        prev.next = delnode.next


if __name__ == "__main__":
    list = [10, 7, 9, 18, 13, 7]
    sl = SinglyLinkedList()
    for i in list:
        sl.append(i)
    print(f"The Singly Linked list after insertion:")
    sl.display()
    print()
    sl.find(18)
    print()
    sl.remove(78)
    print()
    print(f"The Singly Linked list after deletion :")
    sl.display()

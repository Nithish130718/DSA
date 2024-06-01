class Node:
    __slots__ = ["item", "next"]

    def __init__(self, item=None, next=None) -> None:
        self.item, self.next = item, next

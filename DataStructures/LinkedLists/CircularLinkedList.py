
from NodeCreation import Node

class CircularLinkedList:
    def __init__(self) -> None:
        self.size = 0 
        self.head = Node()
        self.head.next = self.head 
        self.tail = self.head 

    
    def isempty(self):
        if self.head.next == self.head:     
            return True
        return False


    def apppend(self, ele):
        temp = Node(ele)
        temp.next = self.head
        self.tail.next = temp
        self.tail = temp 
        self.size += 1
    
    def display(self):
        res = ''
        pos = self.head.next 
        while pos != self.head:
            res += str(pos.item) + ' '
            pos = pos.next 
        return res 


# No change in the insert(), remove() functions -> same as for singlylinkedlist. if the delnode is self.tail handling it is necessary (left as exercise) 
# for find() function change in the while loop will make things work!

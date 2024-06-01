
# Wrapper Approach - List based implentation 

class Queue:
    '''
    This class is an implementation f '''
    def __init__(self):
        self.item = []
    def isempty(self):
        if len(self.item) == 0:
            return True
        return False
    def enqueue(self,ele):
        self.item.append(ele)
    def dequeue(self):
        ele = self.item[0]
        self.item.pop(0)
        return str(ele)
    def __len__(self):
        return len(self.item)
    def __str__(self):
        return str(self.item) 
    def first_ele(self):
        return self.item[0]


if __name__ == '__main__':
    #Checking working of Queue functions
    q = Queue()
    print(q.isempty())
    q.enqueue(10)
    q.enqueue(20)
    print(q)
    print(len(q))
    print(q.first_ele())
    q.dequeue()
    print(q)

class Stack:
    '''
    This class is a python list-based implementation of the stack ADT.
    '''
    def __init__(self):
        self.item = []
    def isempty(self):
        if len(self.item) == 0:
            return True
        return False
    def push(self,ele):
        self.item.append(ele)
    def pop(self):
        ele = self.item[-1]
        self.item.pop()
        return str(ele)
    def __len__(self):
        return len(self.item)
    def __str__(self):
        return str(self.item) 
    def top_ele(self):#peek/peep 
        return self.item[-1]


if __name__ == '__main__':
    #Checking working of Stack functions
    s = Stack()
    print(s.isempty())
    s.push(10)
    s.push(20)
    print(s)
    print(len(s))
    print(s.top_ele())
    s.pop()
    print(s)

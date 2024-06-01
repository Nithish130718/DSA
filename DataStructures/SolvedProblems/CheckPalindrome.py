
"""

Question: To check if a given number is a palindrome or not using an empty stack, queue and their related functions. 
HINT: You are allowed to use list based implementation for the same.

"""

class Stack:
    '''
    This class is an implementation of the stack ADT.
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
    
    #Checking if a number is a palindrome.
    n = input("Enter a number:")
    def palindrome(n):
        s1 = Stack()
        q1 = Queue()
        initial_n, reversed_n = '',''
        for i in n:
            s1.push(int(i))
            q1.enqueue(int(i))
        for i in range(len(n)):
            initial_n +=  q1.dequeue()
            reversed_n += s1.pop() 
        
        if initial_n == reversed_n:
            return 'Yes, its a palindrome'
        else:
            return 'No, its not a palindrome.'   
    print(palindrome(n))

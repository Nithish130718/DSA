'''
This module provides two classes 'Stack' and 'Queue' using the 'Wrapper Approach'.
This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 31st May 2023

Revised on: 03rd June 2023

Original Author: Nithish Kumar S [IT-B, 3122 22 5002 084]
'''


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

    print()
    
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

    print()

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


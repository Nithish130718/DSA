
"""
Question: To check if a given number is a palindrome or not, using an empty stack, queue and their related functions. 
"""

"""
Implementation of stack and queue data structures as classes (as asked) to be included here....
"""

# You can find the wrapper approach implementation of the stack here: https://github.com/Nithish130718/DSA/blob/main/DataStructures/Stacks/Wrapper_Approach.py
# And the implementation of the queue here: https://github.com/Nithish130718/DSA/blob/main/DataStructures/Queues/Wrapper_Approach.py
    

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

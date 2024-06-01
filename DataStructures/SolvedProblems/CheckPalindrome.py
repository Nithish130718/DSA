"""
Question : To check if a given number is a palindrome using a stack and queue, given that you're allowed to use the list-based implementations of the same.
"""

'''
You can find the link-based implementation of the stack [here](https://github.com/Nithish130718/DSA/new/main/DataStructures/Stacks/List_Implentation.py) and queue [here](https://github.com/Nithish130718/DSA/new/main/DataStructures/Queues/List_Implentation.py)
'''

if __name__ == '__main__':
    # Checking if a number is a palindrome.
    n = input("Enter a number:")
    def palindrome(n):
        s1 = Stack()
        q1 = Queue()
        initial_n, reversed_n = '', ''
        for i in n:
            s1.push(int(i))
            q1.enqueue(int(i))
        for i in range(len(n)):
            initial_n += str(q1.dequeue())
            reversed_n += str(s1.pop())
        if initial_n == reversed_n:
            return 'Yes, it\'s a palindrome'
        else:
            return 'No, it\'s not a palindrome.'
    print(palindrome(n))

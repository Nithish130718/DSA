'''
This module provides two classes:
1) A base class 'functions' that is implemented for the constructor and the length function purpose;
2) A child class 'Stack' that evaluates a infix expression by converting it into a postfix expression and returns the result of it.

This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 05th June 2023

Revised on: 05th June 2023

Original Author: Nithish Kumar S [IT-B, 3122 22 5002 084]
'''

class functions:
    '''This base class is implemented just for the sake of declaring the constructor and the __len__ function that returns the length of the 
    stack.'''

    def __init__ (self):
        '''
        The constructor __init__ has two member data / variables as:
        - self.item which is thhe initialization of the stack itself.
        - self.top which points to the len of the stack.
        '''
        self.item = []                #Stack to store the postfix expression.
        self.res = []                 #Stack to perform evaluation and return the result.
        self.top = 0 
    
    def __len__(self):
        '''The __len__ function returns the length of the object (stack) created.'''
        return len(self.item)
    


class Stack(functions):
    ''' 
    The child / derived class 'Stack' contains 4 special methods namely,
    1) 'Postfix' that gives a postfix expression for a given input infix expression,
    2) __getitem__ and __setitem__ to get element of a specified index (here for looping) and to set elements to a particular index (here to replace elements in a stack),
    3) 'calculate' that calculates the result for a given infix expression and values.
    '''

    def postfix(self,exp):
        '''This function 'postfix' converts an input infix expression into a postfix expression.'''

        print('The infix expression given as input is: ',exp)

        global operators                            #making list as global for global scope in upcoming methods.
        operators = ['+','-','*','/','%']
        temp = []
        for i in exp:
            if i not in operators:
                self.item.append(i)
            else:
                temp.append(i)
        temp.sort()                                 #sorting operators' list (which contains operators in given infix expression) as per precedence.
        for i in temp:                              #adding the operators at end of the postfix expression (format).
            self.item.append(i)
        self.top = len(self.item)                   
        return self.item      
    
    def __getitem__(self,index):
        '''The function __getitem__ helps to get the element of a specified index (used in looping here).'''
        return self.item[index]
    

    def __setitem__(self,index,ele):
        '''The function __setitem__ helps to assign an element to an index (here for replacing elements in 'calculate' method).'''
        self.item[index] = ele
        return 
    

    def calculate(self,a=0,b=0,c=0):
        '''
        The function 'calculate' helps to calculate the result of a given infix expression (converted into a postfix equation by previous 
        method) and a given set of values.
        '''
        print('The values of a, b and c are:',a,',',b,',',c)
    
        variables = ['a','b','c']            #list containing the variables in a common infix / postfix expression involving 3 variables.

        #replacing a,b,c by their given set of values accordingly.
        for i in range(len(self)):                      
            if self.item[i] == 'a':
                self.item[i] = a
            elif self.item[i] == 'b':
                self.item[i] = b
            elif self.item[i] == 'c':
                self.item[i] = c
        
        #evaluation of the postfix equation generated for a given set of values.
        for i in self.item:                             
            if i not in operators:                      #if operand -> pushes into the stack.
                self.res.append(i)
            else:                                       #if operator -> pops 2 elements, evaluates and pushes result into the stack.
                operator = i
                change_index = len(self.res) - 2
                pop1 = self.res.pop(change_index+1)
                pop2 = self.res.pop(change_index)
                if operator == '+':
                    temp = pop1+pop2
                elif operator == '-':
                    temp = pop1-pop2
                elif operator == '*':
                    temp = pop1*pop2
                elif operator == '/':
                    temp = pop1/pop2
                elif operator == '%':
                    temp = pop1%pop2
                self.res.insert(change_index,temp)
        
        return self.res[0]                                   #returns result


    def __str__(self):
        '''
        The __str__ method returns the postfix expression.
        '''
        st = ''
        for i in range(len(self)):
            st += str(self.item[i])
        return st
    

#----------------------------------------------------------------DRIVER CODE----------------------------------------------------------------

if __name__ == '__main__':
    #Creating an object instance of class 'Stack'
    obj = Stack()

    #Calling the 'postfix' method to get the postfix expression of an infix expression (passed as an argument). Priniting the same.
    obj.postfix('a+b*c')
    print('The postfix expression for given input is:',obj)

    #To calculate the result for the given infix expression, for a given set of values (now passed as arguments).
    print('The result is:',obj.calculate(9,5,2))


    '''
    ADDITIONAL DRIVER FUNCTIONS:
    
    1) To get the length of the object instance Stack containing the postfix expression: 
       
         print(len(obj)) 

    2) __getitem__ and __setitem__ to perform any referential or assignment operations.
    '''

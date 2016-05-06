"""
-------------------------------------------------------
# stack.py
Class definition for LIFO Stack implemented as a list.
-------------------------------------------------------
Author:  Rick Henderson
Email:   rhenderson@wlu.ca
__updated__ = "2016-05-06"

Notes: 
2016-05-06 __init__, push, pop, peek, and is_empty all working

TODO:
__str__ needs to function.
-------------------------------------------------------
"""

from copy import deepcopy


class Stack:
    """
       Use s = Stack() to initialize the Stack.
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a list.
        Use: s = Stack()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty stack.
        -------------------------------------------------------
        """
        self._values = []
        # print("stack created")

        return

    def __str__(self):
        string_value = ""
        for i in range(len(self._values)):
            string_value = string_value + (", NYI" * i)

        return string_value

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto stack.
        Use: s.push(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the top of the stack.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def pop(self):
        top_value = self._values.pop()
        return top_value

    def peek(self):
        # Pop the top value to return it for peeking
        top_value = self._values.pop()

        # Push the top value back onto the stack so the stack is unchanged
        self.push(top_value)
        return top_value

    def is_empty(self):
        if len(self._values) == 0:
            result = True
        else:
            result = False

        return result

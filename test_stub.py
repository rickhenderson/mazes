"""
-------------------------------------------------------
test_stub.py
General program to test other classes and things.
-------------------------------------------------------
Author:  Rick Henderson
Email:   rhenderson@wlu.ca
__updated__ = "2016-05-06"
-------------------------------------------------------
"""
from stack import Stack

# Create a stack
s = Stack()

# Check for empty stack
print("Stack is empty: {}".format(s.is_empty()))

# Push some items.
s.push(3)
s.push(4)
s.push(77)
print("--- Items pushed into stack.")

# Check for empty stack
print("Stack is empty: {}".format(s.is_empty()))

# Peek
print("The top value is: {}".format(s.peek()))

# Print the stack
print(s)

# Pop something
value = s.pop()
print("Item has been popped.")

# Remove last Values
print("Removing the last items...")
value = s.pop()
value = s.pop()
print("\nStack is empty: {}".format(s.is_empty()))

print(" ** Program complete. **")

# Stack is a type of a data structure.
# Stack follows LIFO principle.
# LIFO stands for "Last in first out."
# Basic operations of stack includes: push, pop, and peak.


# Visual example of a stack.
'''
     |_____element__n______|
     |_____element__three__|
     |_____element__two____|
     |_____element__one____| '''

# Push. Adds data to a stack.
# Pop. Removes the topmost data from stack.
# Peek. Gets the value of topmost data on the stack.

# Using list based implementation to perform stack operations.

# Push, Pop and Peek have a time complexity of O(1) on operations of a stack with array based implemention.


class Stack:

    def create_a_stack(self):

        stack = []

        return stack

    def push(self, stack: list, data):
        stack.append(data)

    def check_stack_length(self, stack: list):

        length_of_the_stack = len(stack)

        return length_of_the_stack == 0

    def pop(self, stack: list):

        if not self.check_stack_length(stack):
            stack.pop()
        else:
            return "Stack is empty."

    def peek(self, stack:list):

        data = stack[-1]

        return data


# Stack class object creation.

stack_obj = Stack()

# Creating a stack.

stack = stack_obj.create_a_stack()

# Pushing data into the stack.

stack_obj.push(stack, 18)
stack_obj.push(stack, 11)

print("Stack with data in it.", stack)

# Peeking into the stack.

top_most_elemet_of_the_stack = stack_obj.peek(stack)

print("Current top most element of the stack", top_most_elemet_of_the_stack)

# Pop elements out of the stack.

stack_obj.pop(stack)

print(f"Stack after performing a pop operation. {stack}")

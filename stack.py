# Name: Calvin Tang

# stack.py
# This module defines the Stack ADT and operations below
# This Stack ADT is implemented by singly linked list nodes

# Functions: 
# Node(): Creates a new Node
# Stack(): Creates a new Stack
# push(x): Inserts x on top of stack
# pop(): Removes and returns the stack's top item
# isEmpty(): Returns true if stack has no items
# getLength(): Returns the number of items in the stack
# peek(): Returns but does not remove the stack's top item
# display(): Prints node items from top to bottom of stack

# Initializing Singly Linked List ADT
class Node:
    # Function: Node object defined for in Singly Linked List ADT
    # Input: value "data" assinged to Node; Output: N/A
    def __init__(self, data):
        self.data = data
        self.next = None

# Initializing Stack ADT, implemented with Singly Linked List
class Stack:
    # Function: Stack object defined by Singly Linked List implementation
    # Input: N/A; Output: N/A
    def __init__(self):
        self.top = None
        self.size = 0

    # Function: push new node onto stack
    # Input: value "x" assigned to new Stack item; Output: N/A
    def push(self, x):
        newNode = Node(x)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.size += 1

    # Function: pop and return the node at top of the stack
    # Input: N/A, Output: value "poppedValue" of popped node
    def pop(self):
        if self.isEmpty():  # creates error if Stack is empty
            raise IndexError("Pop cannot be performed. Too many operators.")
        
        poppedValue = self.top.data
        self.top = self.top.next
        self.size -= 1
        return poppedValue
    
    # Function: checks if stack is empty
    # Input: N/A, Output: "True" if stack is empty otherwise "False"
    def isEmpty(self):
        if self.top is None:
            return True
        return False
    
    # Function: returns number of items in Stack
    # Input: N/A, Output: size of Stack "self.size"
    def getLength(self):
        return self.size
    
    # Function: returns value of top node in Stack
    # Input: N/A, Output: value of top node if Stack not empty "self.top.data"
    def peek(self):  
        if self.isEmpty():
            raise IndexError("Peek cannot be performed. Stack is empty")
        return self.top.data
    
    # Function: display elements in Stack
    # Input: N/A, Output: prints array of stack values in order
    def display(self):
        cur = self.top
        displayElements = []
        while cur:
            displayElements.append(cur.data)
            cur = cur.next
        print("Stack (top to bottom):", " -> ".join(map(str, displayElements)))
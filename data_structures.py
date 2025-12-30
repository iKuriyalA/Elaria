"""
data_structures.py
------------------
All mutable state lives here.
Each structure exposes a common interface:
- execute_command(action, args)
"""

# --------------------------------------------------
# ARRAY
# --------------------------------------------------
class Array:
    def __init__(self):
        self.data = []

    def execute_command(self, action, args):
        if action == "ADD":
            self.data.extend(args)
        elif action == "REMOVE":
            for val in args:
                if val in self.data:
                    self.data.remove(val)
        elif action == "DISPLAY":
            print(self.data)
        else:
            print("Unknown ARRAY command.")


# --------------------------------------------------
# STACK (LIFO)
# --------------------------------------------------
class Stack:
    def __init__(self):
        self.data = []

    def execute_command(self, action, args):
        if action == "PUSH":
            for val in args:
                self.data.append(val)
        elif action == "POP":
            if self.data:
                print("Popped:", self.data.pop())
        elif action == "DISPLAY":
            print(self.data)
        else:
            print("Unknown STACK command.")


# --------------------------------------------------
# QUEUE (FIFO)
# --------------------------------------------------
class Queue:
    def __init__(self):
        self.data = []

    def execute_command(self, action, args):
        if action == "ENQUEUE":
            for val in args:
                self.data.append(val)
        elif action == "DEQUEUE":
            if self.data:
                print("Dequeued:", self.data.pop(0))
        elif action == "DISPLAY":
            print(self.data)
        else:
            print("Unknown QUEUE command.")

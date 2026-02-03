"""
Concrete implementations of data structures.

Each structure:
- Owns its internal state
- Knows how to execute its own commands
- Does NOT worry about parsing or routing
"""

from algorithms import list_diagram_display


class Array:
    def __init__(self):
        self.data = []

    def execute_command(self, action, args):
        if action == "ADD":
            # Dynamic array append (amortized O(1) per element)
            self.data.extend(args)
            print("Added:", args)

        elif action == "REMOVE":
            # Linear scan to find elements
            for v in args:
                if v in self.data:
                    self.data.remove(v)
            print("Removed:", args)

        elif action == "DIAGRAM":
            list_diagram_display(self.data)

        else:
            print("Unknown ARRAY command")


class Stack:
    def __init__(self):
        self.data = []

    def execute_command(self, action, args):
        if action == "PUSH":
            # Push one-by-one to preserve stack order
            for v in args:
                self.data.append(v)
            print("Pushed:", args)

        elif action == "POP":
            if self.data:
                print("Popped:", self.data.pop())

        elif action == "DIAGRAM":
            list_diagram_display(self.data)

        else:
            print("Unknown STACK command")


class Queue:
    def __init__(self):
        self.data = []

    def execute_command(self, action, args):
        if action == "ENQUEUE":
            self.data.extend(args)
            print("Enqueued:", args)

        elif action == "DEQUEUE":
            # pop(0) is O(n), intentionally kept for teaching purposes
            if self.data:
                print("Dequeued:", self.data.pop(0))

        elif action == "DIAGRAM":
            list_diagram_display(self.data)

        else:
            print("Unknown QUEUE command")

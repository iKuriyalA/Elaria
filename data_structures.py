from algorithms import list_diagram_display


class Array:
    def __init__(self):
        self.data = []

    def execute_command(self, action, args):
        if action == "ADD":
            self.data.extend(args)
            print("Added:", args)
        elif action == "REMOVE":
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
            self.data.extend(args)
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
            if self.data:
                print("Dequeued:", self.data.pop(0))
        elif action == "DIAGRAM":
            list_diagram_display(self.data)
        else:
            print("Unknown QUEUE command")

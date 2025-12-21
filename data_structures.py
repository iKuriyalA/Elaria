def list_diagram_display(arr, highlight_index=None):
    top = "┌" + "┬".join(["───" for _ in arr]) + "┐"
    mid = "│" + "│".join([f"{str(val).center(3)}" for val in arr]) + "│"
    bottom = "└" + "┴".join(["───" for _ in arr]) + "┘"

    pointer_line = ""
    if highlight_index is not None:
        spaces = 2 + 4 * highlight_index
        pointer_line = " " * spaces + "↑\n" + " " * spaces + "i\n"

    print(top)
    print(mid)
    print(bottom)

    if highlight_index is not None:
        print(pointer_line)


class Queue:
    def __init__(self):
        self.data = []

    def offer(self, value):
        self.data.append(value)
        print(f"Offered {value} to the queue")

    def poll(self):
        if not self.data:
            print("Queue is empty")
            return None
        value = self.data.pop(0)
        print(f"Polled {value} and removed it from the queue")

    def peek(self, index):
        if not self.data:
            print("Queue is empty")
            return None
        print(f"Value at index {index}: {self.data[index]}")

    def queue_diagram(self):
        print("Queue:")
        list_diagram_display(self.data)

    def execute_command(self, action, args):
        action = action.upper()
        if action == "OFFER":
            for val in args:
                self.offer(val)
        elif action == "POLL":
            self.poll()
        elif action == "PEEK":
            for val in args:
                self.peek(val)
        elif action == "DIAGRAM":
            self.queue_diagram()
        else:
            print(f"Unknown command for Queue: {action}")


class Array:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)
        print(f"Added {value} to array")

    def insert(self, value, index):
        self.data.insert(index, value)
        print(f"Inserted {value} at index {index} in array")

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
            print(f"Removed {value} from array")
        else:
            print(f"{value} not found in array")

    def array_diagram(self):
        print("Array:")
        list_diagram_display(self.data)

    def execute_command(self, action, args):
        action = action.upper()
        if action == "ADD":
            for val in args:
                self.add(val)
        elif action == "INSERT":
            if len(args) >= 2:
                self.insert(int(args[0]), int(args[1]))
        elif action == "REMOVE":
            for val in args:
                self.remove(val)
        elif action == "DIAGRAM":
            self.array_diagram()
        else:
            print(f"Unknown command for Array: {action}")


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        print(f"Pushed {value} to stack")

    def pop(self):
        if not self.data:
            print("Stack is empty")
            return None
        value = self.data.pop()
        print(f"Popped {value} from stack")
        return value

    def stack_diagram(self):
        print("Stack diagram:")
        print("┌───────────────────┐")
        for i, item in enumerate(reversed(self.data)):
            print(f"│ {str(item).center(17)} │")
            if i < len(self.data) - 1:
                print("├───────────────────┤")
        print("└───────────────────┘")

    def execute_command(self, action, args):
        action = action.upper()
        if action == "PUSH":
            for val in args:
                self.push(val)
        elif action == "POP":
            self.pop()
        elif action == "DIAGRAM":
            self.stack_diagram()
        else:
            print(f"Unknown command for Stack: {action}")

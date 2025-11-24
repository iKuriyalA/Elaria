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
        print("Array diagram:")
        for value in enumerate(self.data):
            print(f"{value}", end=" ")
        print()

    def execute_command(self, action, args):
        action = action.upper()
        if action == "ADD":
            for val in args: self.add(val)
        elif action == "INSERT":
            if len(args) >= 2: self.insert(args[0], int(args[1]))
        elif action == "REMOVE":
            for val in args: self.remove(val)
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
            for val in args: self.push(val)
        elif action == "POP":
            self.pop()
        elif action == "DIAGRAM":
            self.stack_diagram()
        else:
            print(f"Unknown command for Stack: {action}")

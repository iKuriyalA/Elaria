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
        else:
            value = self.data.pop()
            print(f"Popped {value} from stack")
            return value

    def show(self):
        print("Stack contents:", self.data)

    def diagram(self):
        print("Stack diagram:")
        for item in reversed(self.data):
            print(f"| {item} |")
            print("-----")

def run_command(command, data_structure):
    parts = command.strip().split()
    if not parts:
        return True  # keep running
    
    action = parts[0].upper()
    
    if action == "CREATE":
        if parts[1].upper() == "STACK":
            data_structure['stack'] = Stack()
            print("Created a new stack")
    
    elif action == "PUSH":
        if 'stack' in data_structure:
            if len(parts) > 1:
                try:
                    value = int(parts[1])
                except ValueError:
                    value = parts[1]  # allow strings too
                data_structure['stack'].push(value)
            else:
                print("Usage: PUSH <value>")
        else:
            print("No stack exists. Create one first.")
    
    elif action == "POP":
        if 'stack' in data_structure:
            data_structure['stack'].pop()
        else:
            print("No stack exists. Create one first.")
    
    elif action == "SHOW":
        if 'stack' in data_structure:
            data_structure["stack"].show()
        else:
            print("No stack exists. Create one first.")
    
    elif action == "EXIT":
        return False  # stop running
    
    elif action == "DIAGRAM":
        if len(parts) == 1:
            print("No given data structure to visualize!")
            return True
        elif parts[1] == "STACK":  
            if 'stack' in data_structure:
             data_structure["stack"].diagram()
            else:
              print("No stack exists. Create one first.")
    else:
        print("Unknown command:", action)

    return True

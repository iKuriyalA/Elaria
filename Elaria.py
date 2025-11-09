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
            print(f"{value}", end = " ")
        print()
    
    def execute_command(self, action, args):
        action = action.upper()
        if action == "ADD":
            for val in args:
                self.add(val)
        elif action == "INSERT":
            if len(args) >= 2:
                self.insert(args[0], int(args[1]))
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
       else:
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


def split_list_vals(values):
   vals = values[1:len(values)-1]
   f_vals = vals.split(",")
   return f_vals


def run_command(command, data_structure):
    parts = command.strip().split(maxsplit=2)
    if not parts:
        return True 
        
    action = parts[0].upper()

    if action == "CREATE":
        if len(parts) < 2:
            print("There is nothing to create")
            return True
        
        ds_type = parts[1].upper()
        if ds_type == "STACK":
            data_structure["stack"] = Stack()
            print("Created a new stack")
        elif ds_type == "ARRAY":
            data_structure["array"] = Array()
            print("Created a new array")
        else:
            print("Not currently supported. Try another data structure.")
        return True

    elif action == "EXIT":
        return False
    
    ds_type = action.lower()

    if ds_type not in data_structure:
        print(f"No {ds_type} exists. Create one first..")
        return True

    if len(parts) < 2:
        print("Invalid syntax. Example: ARRAY ADD [1,2,3]")
        return True

    sub_action = parts[1].upper()
    args = []
    if len(parts) == 3:
        args = split_list_vals(parts[2])

    data_structure[ds_type].execute_command(sub_action, args)
    return True

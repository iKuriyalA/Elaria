from data_structures import Array, Stack
from algorithms import SearchAlgorithms, list_diagram_display


def split_list_vals(values):
    vals = values[1:-1]
    return [v.strip() for v in vals.split(",")]


def run_command(command, data_structures):
    parts = command.strip().split(maxsplit=2)
    if not parts:
        return True

    action = parts[0].upper()

    if action == "CREATE":
        if len(parts) < 2:
            print("There is nothing to create")
            return True
        
        ds_type = parts[1].lower()
        if ds_type == "stack":
            data_structures["stack"] = Stack()
            print("Created a new stack")
        elif ds_type == "array":
            data_structures["array"] = Array()
            print("Created a new array")
        else:
            print("Unsupported data structure.")
        return True

    if action == "EXIT":
        return False

    ds_type = action.lower()

    if ds_type in ("linearsearch", "binarysearch"):
        # algorithm command
        return run_algorithm_command(ds_type, parts)

    if ds_type not in data_structures:
        print(f"No {ds_type} exists. Create one first.")
        return True

    if len(parts) < 2:
        print("Invalid syntax. Example: ARRAY ADD [1,2,3]")
        return True

    sub_action = parts[1].upper()
    args = split_list_vals(parts[2]) if len(parts) == 3 else []

    data_structures[ds_type].execute_command(sub_action, args)
    return True


def run_algorithm_command(algo, parts):
    if len(parts) < 3:
        print("Usage: binarysearch [list] target")
        return True
    # Example user input:
    # binarysearch [1,2,3,4] 3
    
    array_str, target = parts[1], parts[2]
    arr = split_list_vals(array_str)
    arr = [int(x) for x in arr]

    target = int(target)

    if algo == "linearsearch":
        SearchAlgorithms.linear_search(arr, target)
    else:
        SearchAlgorithms.binary_search(arr, target)


    data_structure[ds_type].execute_command(sub_action, args)
    return True

class SearchAlgorithms:

    def list_diagram_display(arr, highlight_index=None):
    top = "┌" + "┬".join(["───" for val in arr]) + "┐"
    mid = "│" + "│".join([f"{str(val).center(3)}" for val in arr]) + "│"
    bottom = "└" + "┴".join(["───" for val in arr]) + "┘"

    pointer_line = ""
    if highlight_index is not None:
        spaces = 2 + 4 * highlight_index
        pointer_line = " " * spaces + "↑\n" + " " * spaces + "i\n"

    print(top)
    print(mid)
    print(bottom)
    if highlight_index is not None:
        print(pointer_line)

    def linear_search(arr, target):
        visual = []
        for index, value in enumerate(arr):
            list_diagram_display(arr, index)
            if value == target:
                print(f"{target} found at index {index}")
                return index
        return -1

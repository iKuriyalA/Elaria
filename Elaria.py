# elaria.py
from data_structures import Array, Stack
from algorithms import SearchAlgorithms


def split_list_vals(values):
    # expects something like "[1,2,3]"
    vals = values[1:-1]
    return [v.strip() for v in vals.split(",") if v.strip()]


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
        print("Usage: linearsearch [list] target")
        return True

    array_str, target = parts[1], parts[2]

    try:
        arr = [int(x) for x in split_list_vals(array_str)]
        target = int(target)
    except ValueError:
        print("List and target must be integers.")
        return True

    if algo == "linearsearch":
        SearchAlgorithms.linear_search(arr, target)
    else:
        SearchAlgorithms.binary_search(arr, target)

    return True

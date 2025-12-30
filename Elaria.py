from data_structures import Array, Stack, Queue
from algorithms import (
    SearchAlgorithms,
    SortingAlgorithms,
    list_diagram_display
)


def split_list_vals(values):
    vals = values[1:-1]
    return [v.strip() for v in vals.split(",")]


def run_command(command, data_structures):
    parts = command.strip().split(maxsplit=2)
    if not parts:
        return True

    action = parts[0].upper()

    # -------------------------
    # CREATE
    # -------------------------
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
        elif ds_type == "queue":
            data_structures["queue"] = Queue()
            print("Created a new queue")
        else:
            print("Unsupported data structure.")
        return True

    # EXIT
    if action == "EXIT":
        return False

    # -------------------------
    # ALGORITHMS
    # -------------------------
    algo = action.lower()
    if algo in (
        "linearsearch",
        "binarysearch",
        "insertionsort",
        "selectionsort",
        "mergesort",
    ):
        return run_algorithm_command(algo, parts)

    # -------------------------
    # DATA STRUCTURES
    # -------------------------
    ds_type = action.lower()
    if ds_type not in data_structures:
        print(f"No {ds_type} exists. Create one first.")
        return True

    if len(parts) < 2:
        print("Invalid syntax.")
        return True

    sub_action = parts[1].upper()
    args = split_list_vals(parts[2]) if len(parts) == 3 else []
    data_structures[ds_type].execute_command(sub_action, args)
    return True


def run_algorithm_command(algo, parts):
    if len(parts) < 2:
        print("Usage: algorithm [list] (target)")
        return True

    arr = split_list_vals(parts[1])
    arr = [int(x) for x in arr]

    # SEARCH
    if algo == "linearsearch":
        target = int(parts[2])
        result = SearchAlgorithms.linear_search(arr, target)
        if result == -1:
            print(f"{target} not found.")
        return True

    if algo == "binarysearch":
        target = int(parts[2])
        result = SearchAlgorithms.binary_search(arr, target)
        if result == -1:
            print(f"{target} not found.")
        return True

    # SORTING
    if algo == "insertionsort":
        SortingAlgorithms.insertion_sort_descending(arr)

    elif algo == "selectionsort":
        SortingAlgorithms.selection_sort_desending(arr)

    elif algo == "mergesort":
        result = SortingAlgorithms.mergesort(arr)
        print("Finalized Array (using merge sort):")
        list_diagram_display(result)

    return True

# Central command router (no algorithms or data stored here)

from data_structures import Array, Stack, Queue
from algorithms import SearchAlgorithms, SortingAlgorithms


def split_list_vals(values):
    # Convert "[1,2,3]" → [1, 2, 3]
    values = values.strip()
    if not values.startswith("[") or not values.endswith("]"):
        raise ValueError("Invalid list format")
    inner = values[1:-1].strip()
    return [] if inner == "" else [int(v.strip()) for v in inner.split(",")]


def run_command(command, data_structures):
    if not command.strip():
        return True

    parts = command.split(maxsplit=1)
    action = parts[0].upper()

    # Exit program
    if action == "EXIT":
        return False

    # Create data structure
    if action == "CREATE":
        ds = parts[1].lower()
        data_structures[ds] = {"array": Array, "stack": Stack, "queue": Queue}[ds]()
        print(f"Created {ds}")
        return True

    # Algorithm commands
    if action == "ALGO":
        return run_algorithm_command(parts[1])

    # Data structure commands
    ds = action.lower()
    if ds not in data_structures:
        print(f"No {ds} exists.")
        return True

    sub = parts[1].split(maxsplit=1)
    action = sub[0].upper()
    args = split_list_vals(sub[1]) if len(sub) > 1 else []

    data_structures[ds].execute_command(action, args)
    return True


def run_algorithm_command(command):
    parts = command.split(maxsplit=1)
    algo = parts[0].lower()
    arr = split_list_vals(parts[1])

    if algo == "linearsearch":
        SearchAlgorithms.linear_search(arr[:-1], arr[-1])
    elif algo == "binarysearch":
        SearchAlgorithms.binary_search(arr[:-1], arr[-1])
    elif algo == "insertionsort":
        SortingAlgorithms.insertion_sort_descending(arr)
    elif algo == "selectionsort":
        SortingAlgorithms.selection_sort_descending(arr)
    elif algo == "mergesort":
        SortingAlgorithms.display(SortingAlgorithms.merge_sort(arr))
    else:
        print("Unknown algorithm")

    return True

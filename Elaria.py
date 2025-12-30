"""
Elaria.py
---------
Central command engine.

Responsibilities:
- Parse user input
- Route commands to data structures OR algorithms
- Enforce consistent CLI syntax
"""

from data_structures import Array, Stack, Queue
from algorithms import SearchAlgorithms


# --------------------------------------------------
# Utility: safely parse lists like [1, 2, 3]
# --------------------------------------------------
def split_list_vals(values):
    """
    Converts a string like "[1, 2, 3]" into [1, 2, 3]

    Why this exists:
    - prevents fragile string parsing
    - centralizes validation logic
    """
    values = values.strip()

    if not values.startswith("[") or not values.endswith("]"):
        raise ValueError("List must be written as [1,2,3]")

    inner = values[1:-1].strip()

    if inner == "":
        return []

    return [int(v.strip()) for v in inner.split(",")]


# --------------------------------------------------
# Main Command Dispatcher
# --------------------------------------------------
def run_command(command, data_structures):
    """
    Top-level interpreter.
    Decides what category a command belongs to:
    - CREATE
    - ALGO
    - DATA STRUCTURE
    """
    if not command.strip():
        return True

    parts = command.strip().split(maxsplit=1)
    action = parts[0].upper()

    # -------------------------
    # EXIT PROGRAM
    # -------------------------
    if action == "EXIT":
        return False

    # -------------------------
    # CREATE DATA STRUCTURE
    # -------------------------
    if action == "CREATE":
        if len(parts) < 2:
            print("Usage: CREATE stack|array|queue")
            return True

        ds = parts[1].lower()

        if ds == "array":
            data_structures["array"] = Array()
        elif ds == "stack":
            data_structures["stack"] = Stack()
        elif ds == "queue":
            data_structures["queue"] = Queue()
        else:
            print("Unknown data structure.")
            return True

        print(f"Created {ds}")
        return True

    # -------------------------
    # ALGORITHMS
    # -------------------------
    if action == "ALGO":
        if len(parts) < 2:
            print("Usage: ALGO <algorithm> [list] target")
            return True
        return run_algorithm_command(parts[1])

    # -------------------------
    # DATA STRUCTURE COMMANDS
    # -------------------------
    ds_type = action.lower()

    if ds_type not in data_structures:
        print(f"No {ds_type} exists. Create it first.")
        return True

    if len(parts) < 2:
        print("Invalid command.")
        return True

    subparts = parts[1].split(maxsplit=1)
    sub_action = subparts[0].upper()
    args = split_list_vals(subparts[1]) if len(subparts) > 1 else []

    data_structures[ds_type].execute_command(sub_action, args)
    return True


# --------------------------------------------------
# Algorithm Command Handler
# --------------------------------------------------
def run_algorithm_command(command):
    """
    Handles:
    ALGO linearsearch [1,2,3] 2
    ALGO binarysearch [1,2,3] 2
    """
    parts = command.split(maxsplit=2)

    if len(parts) < 3:
        print("Usage: ALGO linearsearch [list] target")
        return True

    algo = parts[0].lower()

    try:
        arr = split_list_vals(parts[1])
        target = int(parts[2])
    except ValueError as e:
        print(e)
        return True

    if algo == "linearsearch":
        index = SearchAlgorithms.linear_search(arr, target)
    elif algo == "binarysearch":
        index = SearchAlgorithms.binary_search(arr, target)
    else:
        print("Unknown algorithm.")
        return True

    if index == -1:
        print(f"{target} not found.")
    else:
        print(f"{target} found at index {index}.")

    return True

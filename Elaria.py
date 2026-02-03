from data_structures import Array, Stack, Queue

from algorithms import (
    linear_search,
    binary_search,
    insertion_sort_descending,
    selection_sort_descending,
    merge_sort_visual
)

from complexities import ALGORITHM_COMPLEXITY, DS_COMPLEXITY
from learn_mode import LearnMode

"""
Central command router for the Elaria language.

Responsibilities:
- Parse user input
- Decide what category the command belongs to
- Dispatch execution to the correct module
- Display time complexity metadata
"""
def parse_list(text):
    """
    Converts a string like "[1, 2, 3]" into a Python list [1, 2, 3].

    Centralized parsing so all commands behave consistently.
    """
    text = text.strip()

    if not (text.startswith("[") and text.endswith("]")):
        raise ValueError("List must be in [1,2,3] format")

    inner = text[1:-1].strip()

    # Handle empty list
    if not inner:
        return []

    try:
        return [int(x.strip()) for x in inner.split(",")]
    except ValueError:
        raise ValueError("List values must be integers")



def show_help():
    """
    Displays the language reference.
    This is intentionally verbose since Elaria is a learning tool.
    """
    print("""
================= ELARIA HELP =================

--- DATA STRUCTURES ---
CREATE STACK
CREATE QUEUE
CREATE ARRAY

STACK PUSH [1,2,3]
STACK POP
QUEUE ENQUEUE [1,2,3]
QUEUE DEQUEUE
ARRAY ADD [1,2,3]
ARRAY REMOVE [2]
<structure> DIAGRAM

--- SEARCH ---
LINEARSEARCH [1,2,3,4,5] 4
BINARYSEARCH [1,2,3,4,5] 4

--- SORT ---
INSERTIONSORT [5,1,4,2]
SELECTIONSORT [5,1,4,2]
MERGESORT [5,1,4,2]

--- LEARNING ---
LEARN
LEARN STACK | QUEUE | ARRAY | SEARCH | SORT

--- SYSTEM ---
HELP
EXIT

===============================================
""")


def run_command(command, data_structures):
    """
    Main interpreter loop logic.
    Returns False only when the program should exit.
    """

    # Ignore empty input
    if not command.strip():
        return True

    # Split command into main keyword and the rest
    parts = command.strip().split(maxsplit=1)
    cmd = parts[0].upper()

    # ---------- SYSTEM COMMANDS ----------
    if cmd == "EXIT":
        return False

    if cmd == "HELP":
        show_help()
        return True

    # ---------- LEARN MODE INTERCEPT ----------
    if "_learn" in data_structures:
        learn = data_structures["_learn"]

        if not learn.validate(command):
            return True

        if learn.finished():
            del data_structures["_learn"]
            return True

        learn.show_prompt()


    # ---------- CREATE DATA STRUCTURES ----------
    if cmd == "CREATE":
        if len(parts) < 2:
            print("Specify what to create")
            return True

        name = parts[1].lower()

        # Factory-style creation
        if name == "stack":
            data_structures["stack"] = Stack()
        elif name == "queue":
            data_structures["queue"] = Queue()
        elif name == "array":
            data_structures["array"] = Array()
        else:
            print("Unknown data structure")
            return True

        print(f"{name.capitalize()} created")
        return True

    # ---------- SEARCH ALGORITHMS ----------
    if cmd in ("LINEARSEARCH", "BINARYSEARCH"):
        rest = parts[1]
        list_part, target = rest.rsplit(maxsplit=1)

        arr = parse_list(list_part)
        target = int(target)

        # Binary search requires sorted input
        if cmd == "LINEARSEARCH":
            linear_search(arr, target)
        else:
            arr.sort()
            binary_search(arr, target)

        # Show theoretical time complexity
        ALGORITHM_COMPLEXITY[cmd].display()
        return True

    # ---------- SORTING ALGORITHMS ----------
    if cmd in ("INSERTIONSORT", "SELECTIONSORT", "MERGESORT"):
        arr = parse_list(parts[1])

        if cmd == "INSERTIONSORT":
            insertion_sort_descending(arr)
        elif cmd == "SELECTIONSORT":
            selection_sort_descending(arr)
        else:
            merge_sort_visual(arr)

        ALGORITHM_COMPLEXITY[cmd].display()
        return True

    # ---------- DATA STRUCTURE OPERATIONS ----------
    ds_name = cmd.lower()

    if ds_name not in data_structures:
        print(f"{ds_name} does not exist")
        return True

    if len(parts) < 2:
        print("Missing command")
        return True

    # Extract operation and arguments
    subcmd, *rest = parts[1].split(maxsplit=1)
    args = parse_list(rest[0]) if rest else []

    action = subcmd.upper()

    # Delegate behavior to the data structure itself
    data_structures[ds_name].execute_command(action, args)

    # Display time complexity metadata (not measured runtime)
    ds_upper = ds_name.upper()
    if ds_upper in DS_COMPLEXITY and action in DS_COMPLEXITY[ds_upper]:
        print(f"Time Complexity: {DS_COMPLEXITY[ds_upper][action]}")

    return True

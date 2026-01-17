# Central command router

from data_structures import Array, Stack, Queue
from algorithms import (
    linear_search,
    binary_search,
    insertion_sort_descending,
    selection_sort_descending,
    merge_sort_visual
)
from learn_mode import LearnMode


def parse_list(text):
    text = text.strip()
    if not (text.startswith("[") and text.endswith("]")):
        raise ValueError("List must be in [1,2,3] format")
    inner = text[1:-1].strip()
    return [] if inner == "" else [int(x.strip()) for x in inner.split(",")]


def show_help():
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

--- SEARCH ALGORITHMS ---
LINEARSEARCH [1,2,3,4,5] 4
BINARYSEARCH [1,2,3,4,5] 4

--- SORTING ALGORITHMS ---
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
    if not command.strip():
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

    parts = command.strip().split(maxsplit=1)
    cmd = parts[0].upper()

    # ---------------- SYSTEM ----------------
    if cmd == "EXIT":
        return False

    if cmd == "HELP":
        show_help()
        return True

    # ---------------- LEARN ----------------
    if cmd == "LEARN":
        topic = parts[1].strip().upper() if len(parts) > 1 else None
        data_structures["_learn"] = LearnMode(topic)
        data_structures["_learn"].show_prompt()
        return True

    # ---------------- CREATE ----------------
    if cmd == "CREATE":
        name = parts[1].strip().lower()
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

    # ---------------- SEARCH ----------------
    if cmd in ("LINEARSEARCH", "BINARYSEARCH"):
        rest = parts[1]
        list_part, target = rest.rsplit(maxsplit=1)
        arr = parse_list(list_part)
        target = int(target)

        if cmd == "LINEARSEARCH":
            linear_search(arr, target)
        else:
            arr.sort()
            binary_search(arr, target)

        return True

    # ---------------- SORT ----------------
    if cmd in ("INSERTIONSORT", "SELECTIONSORT", "MERGESORT"):
        arr = parse_list(parts[1])

        if cmd == "INSERTIONSORT":
            insertion_sort_descending(arr)
        elif cmd == "SELECTIONSORT":
            selection_sort_descending(arr)
        else:
            merge_sort_visual(arr)

        return True

    # ---------------- DATA STRUCTURES ----------------
    ds_name = cmd.lower()
    if ds_name not in data_structures:
        print(f"{ds_name} does not exist")
        return True

    subcmd, *rest = parts[1].split(maxsplit=1)
    args = parse_list(rest[0]) if rest else []

    data_structures[ds_name].execute_command(subcmd.upper(), args)
    return True

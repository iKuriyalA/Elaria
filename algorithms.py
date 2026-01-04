import time


def list_diagram_display(arr, i=None):
    top = "┌" + "┬".join(["───"] * len(arr)) + "┐"
    mid = "│" + "│".join(str(v).center(3) for v in arr) + "│"
    bot = "└" + "┴".join(["───"] * len(arr)) + "┘"

    print(top)
    print(mid)
    print(bot)

    if i is not None:
        print(" " * (2 + 4 * i) + "↑")

    print()
    time.sleep(0.4)


# ---------------- SEARCH ----------------
def linear_search(arr, target):
    print("Linear Search\n")
    for i, v in enumerate(arr):
        list_diagram_display(arr, i)
        if v == target:
            print(f"Found at index {i}")
            return
    print("Not found")


def binary_search(arr, target):
    print("Binary Search\n")
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        list_diagram_display(arr, m)
        if arr[m] == target:
            print(f"Found at index {m}")
            return
        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    print("Not found")


# ---------------- SORT ----------------
def insertion_sort_descending(arr):
    print("Insertion Sort (Descending)\n")
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] < arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            list_diagram_display(arr, j)
            j -= 1
    list_diagram_display(arr)


def selection_sort_descending(arr):
    print("Selection Sort (Descending)\n")
    for i in range(len(arr)):
        max_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_i]:
                max_i = j
        arr[i], arr[max_i] = arr[max_i], arr[i]
        list_diagram_display(arr, i)


def merge_sort_visual(arr):
    print("Merge Sort\n")
    result = merge_sort(arr)
    list_diagram_display(result)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        list_diagram_display(merged + left + right)

    return merged + left + right

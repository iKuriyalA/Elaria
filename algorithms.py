"""
Algorithm implementations used by Elaria.

These are intentionally straightforward and readable,
not hyper-optimized, since Elaria is educational.
"""

def list_diagram_display(lst):
    """Simple ASCII visualization of a list"""
    print("Diagram:")
    for i, v in enumerate(lst):
        print(f"[{i}] -> {v}")


def linear_search(arr, target):
    """Checks each element until target is found"""
    for i, v in enumerate(arr):
        if v == target:
            print(f"Found {target} at index {i}")
            return
    print("Not found")


def binary_search(arr, target):
    """Searches a sorted array by halving the search space"""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print("Not found")


def insertion_sort_descending(arr):
    """Builds a sorted list by inserting elements one at a time"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    print("Sorted:", arr)


def selection_sort_descending(arr):
    """Selects the largest remaining element each pass"""
    n = len(arr)

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    print("Sorted:", arr)


def merge_sort_visual(arr):
    """Divide-and-conquer sorting algorithm"""

    def merge_sort(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])

        return merge(left, right)

    def merge(l, r):
        result = []
        while l and r:
            result.append(l.pop(0) if l[0] > r[0] else r.pop(0))
        result.extend(l or r)
        return result

    print("Sorted:", merge_sort(arr))

# Search and sorting algorithms with visualization

import time


def list_diagram_display(arr, i=None, j=None):
    # Draw array and optional pointers
    top = "┌" + "┬".join(["───"] * len(arr)) + "┐"
    mid = "│" + "│".join(str(v).center(3) for v in arr) + "│"
    bot = "└" + "┴".join(["───"] * len(arr)) + "┘"

    print(top)
    print(mid)
    print(bot)

    if i is not None:
        print(" " * (2 + 4 * i) + "↑ i")
    if j is not None:
        print(" " * (2 + 4 * j) + "↑ j")

    print()
    time.sleep(0.3)


class SearchAlgorithms:

    @staticmethod
    def linear_search(arr, target):
        for i, v in enumerate(arr):
            list_diagram_display(arr, i)
            if v == target:
                print(f"Found at index {i}")
                return i
        print("Not found")
        return -1

    @staticmethod
    def binary_search(arr, target):
        arr.sort()
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            list_diagram_display(arr, m)
            if arr[m] == target:
                print(f"Found at index {m}")
                return m
            l, r = (m + 1, r) if arr[m] < target else (l, m - 1)
        print("Not found")
        return -1


class SortingAlgorithms:

    @staticmethod
    def insertion_sort_descending(arr):
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j - 1] < arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                list_diagram_display(arr, j)
                j -= 1
        list_diagram_display(arr)

    @staticmethod
    def selection_sort_descending(arr):
        for i in range(len(arr)):
            max_i = i
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[max_i]:
                    max_i = j
                    list_diagram_display(arr, i, max_i)
            arr[i], arr[max_i] = arr[max_i], arr[i]
            list_diagram_display(arr, i)

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        return SortingAlgorithms.merge(
            SortingAlgorithms.merge_sort(arr[:mid]),
            SortingAlgorithms.merge_sort(arr[mid:])
        )

    @staticmethod
    def merge(a, b):
        res = []
        while a and b:
            res.append(a.pop(0) if a[0] < b[0] else b.pop(0))
        return res + a + b

    @staticmethod
    def display(arr):
        list_diagram_display(arr)

# --------------------------------------------------
# Search Algorithms
# --------------------------------------------------
class SearchAlgorithms:

    @staticmethod
    def linear_search(arr, target):
        """
        Time: O(n)
        Space: O(1)
        """
        print("Linear Search:\n")
        for i in range(len(arr)):
            list_diagram_display(arr, i)
            if arr[i] == target:
                return i
        return -1

    @staticmethod
    def binary_search(arr, target):
        """
        Time: O(log n)
        Space: O(1)

        NOTE:
        Array must be sorted.
        """
        print("Binary Search:\n")
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            list_diagram_display(arr, mid)

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

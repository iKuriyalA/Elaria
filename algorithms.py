"""
algorithms.py
-------------
Contains all algorithm logic + visualizations.
Algorithms NEVER modify program state.
"""

import time


# --------------------------------------------------
# Visualization Helper
# --------------------------------------------------
def list_diagram_display(arr, highlight_index=None):
    """
    Draws an ASCII array diagram.
    Optionally highlights a single index.
    """
    top = "┌" + "┬".join(["───"] * len(arr)) + "┐"

    mid = "│"
    for i, val in enumerate(arr):
        if i == highlight_index:
            mid += f"\033[92m{str(val).center(3)}\033[0m│"
        else:
            mid += f"{str(val).center(3)}│"

    bottom = "└" + "┴".join(["───"] * len(arr)) + "┘"

    print(top)
    print(mid)
    print(bottom)
    print()
    time.sleep(0.5)


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

def list_diagram_display(arr, highlight_index=None):
    top = "┌" + "┬".join(["───" for _ in arr]) + "┐"
    mid = "│" + "│".join([f"{str(val).center(3)}" for val in arr]) + "│"
    bottom = "└" + "┴".join(["───" for _ in arr]) + "┘"

    pointer_line = ""
    if highlight_index is not None:
        spaces = 2 + 4 * highlight_index
        pointer_line = " " * spaces + "↑\n" + " " * spaces + "i\n"

    print(top)
    print(mid)
    print(bottom)

    if highlight_index is not None:
        print(pointer_line)


class SearchAlgorithms:
    @staticmethod
    def linear_search(arr, target):
        for index, value in enumerate(arr):
            list_diagram_display(arr, index)
            if value == target:
                print(f"{target} found at index {index}")
                return index
        return -1

    @staticmethod
    def binary_search(arr, target):
        arr = sorted(arr)
        print("Sorted Array:")
        list_diagram_display(arr)

        left, right = 0, len(arr) - 1
        counter = 0
        while left <= right:
            mid = (left + right) // 2
            counter += 1

            print(f"Iteration {counter}:")
            list_diagram_display(arr, mid)

            if arr[mid] == target:
                print(f"Found {target} in {counter} iterations.")
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

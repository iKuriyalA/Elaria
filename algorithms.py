def list_diagram_display(arr, highlight_index=None, highlight_2nd_index=None):
    top = "┌" + "┬".join(["───" for _ in arr]) + "┐"
    mid = "│" + "│".join([f"{str(val).center(3)}" for val in arr]) + "│"
    bottom = "└" + "┴".join(["───" for _ in arr]) + "┘"

    print(top)
    print(mid)
    print(bottom)

    if highlight_index is not None:
        spaces = 2 + 4 * highlight_index
        print(" " * spaces + "↑")
        print(" " * spaces + "i")

    if highlight_2nd_index is not None:
        spaces = 2 + 4 * highlight_2nd_index
        print(" " * spaces + "↑")
        print(" " * spaces + "j")


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


class SortingAlgorithms:
    @staticmethod
    def insertion_sort_descending(arr):
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j - 1] < arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                list_diagram_display(arr, j)
                j -= 1
        print("Finalized Array (using descending insertion sort algorithm):")
        list_diagram_display(arr)

    @staticmethod
    def selection_sort_desending(arr):
        for i in range(len(arr)):
            j = i
            for l in range(i + 1, len(arr)):
                if arr[l] > arr[j]:
                    j = l
                    list_diagram_display(arr, i, j)

            if j != i:
                arr[i], arr[j] = arr[j], arr[i]
                list_diagram_display(arr, i)

        print("Finalized Array (using descending selection sort algorithm):")
        list_diagram_display(arr)

    @staticmethod
    def mergesort(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = SortingAlgorithms.mergesort(a[:mid])
        right = SortingAlgorithms.mergesort(a[mid:])
        return SortingAlgorithms.merge(left, right)

    @staticmethod
    def merge(a, b):
        c = []
        while a and b:
            if a[0] > b[0]:
                c.append(b.pop(0))
            else:
                c.append(a.pop(0))
        c.extend(a)
        c.extend(b)
        return c

"""
Stores theoretical time complexity metadata.

Important:
- This does NOT measure runtime
- It represents Big-O behavior
"""

class Complexity:
    def __init__(self, best=None, average=None, worst=None):
        self.best = best
        self.average = average
        self.worst = worst

    def display(self):
        print("Time Complexity:")
        if self.best:
            print(f"  Best:    {self.best}")
        if self.average:
            print(f"  Average: {self.average}")
        if self.worst:
            print(f"  Worst:   {self.worst}")


ALGORITHM_COMPLEXITY = {
    "LINEARSEARCH": Complexity("O(1)", "O(n)", "O(n)"),
    "BINARYSEARCH": Complexity("O(1)", "O(log n)", "O(log n)"),
    "INSERTIONSORT": Complexity("O(n)", "O(n^2)", "O(n^2)"),
    "SELECTIONSORT": Complexity("O(n^2)", "O(n^2)", "O(n^2)"),
    "MERGESORT": Complexity("O(n log n)", "O(n log n)", "O(n log n)")
}

DS_COMPLEXITY = {
    "STACK": {"PUSH": "O(1)", "POP": "O(1)"},
    "QUEUE": {"ENQUEUE": "O(1)", "DEQUEUE": "O(n)"},
    "ARRAY": {"ADD": "O(k)", "REMOVE": "O(n)"}
}

"""
LearnMode for Elaria
====================

- Step-based interactive lessons for STACK, QUEUE, ARRAY, SEARCH, and SORT
- Guides the user to type the correct commands in order
- Works with the main REPL and time complexity system
"""

class LearnMode:
    def __init__(self, topic=None):
        self.step = 0              # Tracks current step in the lesson
        self.topic = topic         # Current topic (STACK, QUEUE, etc.)
        self.steps = self._build_steps()  # Generate lesson steps

    def _build_steps(self):
        """
        Generates a list of steps for the selected topic.
        Each step is a dictionary:
            "prompt" - instruction shown to the user
            "expect" - exact command the user must type (or None for free actions)
        """
        # Default prompt if no topic selected
        if self.topic is None:
            return [{
                "prompt": (
                    "Choose a topic:\n"
                    "LEARN STACK\n"
                    "LEARN QUEUE\n"
                    "LEARN ARRAY\n"
                    "LEARN SEARCH\n"
                    "LEARN SORT"
                ),
                "expect": None  # No command expected, just info
            }]

        # Predefined lessons per topic
        lessons = {
            "STACK": [
                ("Create a stack.\nType: CREATE STACK", "CREATE STACK"),
                ("Push values.\nType: STACK PUSH [1,2,3]", "STACK PUSH [1,2,3]"),
                ("Stacks are LIFO.\nType: STACK POP", "STACK POP"),
                ("Visualize the stack.\nType: STACK DIAGRAM", "STACK DIAGRAM"),
            ],
            "QUEUE": [
                ("Create a queue.\nType: CREATE QUEUE", "CREATE QUEUE"),
                ("Enqueue values.\nType: QUEUE ENQUEUE [1,2,3]", "QUEUE ENQUEUE [1,2,3]"),
                ("Queues are FIFO.\nType: QUEUE DEQUEUE", "QUEUE DEQUEUE"),
                ("Visualize the queue.\nType: QUEUE DIAGRAM", "QUEUE DIAGRAM"),
            ],
            "ARRAY": [
                ("Create an array.\nType: CREATE ARRAY", "CREATE ARRAY"),
                ("Add values.\nType: ARRAY ADD [1,2,3]", "ARRAY ADD [1,2,3]"),
                ("Remove a value.\nType: ARRAY REMOVE [2]", "ARRAY REMOVE [2]"),
                ("Visualize the array.\nType: ARRAY DIAGRAM", "ARRAY DIAGRAM"),
            ],
            "SEARCH": [
                ("Linear Search.\nType: LINEARSEARCH [3,1,4,2] 4",
                 "LINEARSEARCH [3,1,4,2] 4"),
                ("Binary Search.\nType: BINARYSEARCH [1,2,3,4,5] 3",
                 "BINARYSEARCH [1,2,3,4,5] 3"),
            ],
            "SORT": [
                ("Insertion Sort.\nType: INSERTIONSORT [5,3,4,1]",
                 "INSERTIONSORT [5,3,4,1]"),
                ("Selection Sort.\nType: SELECTIONSORT [5,1,4,2]",
                 "SELECTIONSORT [5,1,4,2]"),
                ("Merge Sort.\nType: MERGESORT [6,2,8,1]",
                 "MERGESORT [6,2,8,1]"),
            ],
        }

        # Convert each tuple into a step dict
        steps = [{"prompt": p, "expect": e} for p, e in lessons.get(self.topic, [])]

        # Add final completion step
        steps.append({
            "prompt": f"{self.topic} lesson complete!\nType LEARN to choose another topic.",
            "expect": None
        })

        return steps

    def show_prompt(self):
        """Prints the current step prompt to the user"""
        print(f"\n[LEARN] {self.steps[self.step]['prompt']}")

    def validate(self, command):
        """
        Checks if the user command matches the expected step.
        - If None, accepts any input and advances
        - If correct, advances
        - If wrong, blocks execution and prints warning
        """
        expected = self.steps[self.step]["expect"]

        # Free step (like info or completion)
        if expected is None:
            self.step += 1          # Advance step so finished() can trigger
            return True

        # Correct command typed
        if command.strip().upper() == expected:
            self.step += 1
            return True

        # User typed wrong command
        print("[LEARN] Follow the instruction exactly.")
        return False

    def finished(self):
        """
        Returns True if all steps completed
        This allows Elaria to automatically exit Learn Mode
        """
        return self.step >= len(self.steps)

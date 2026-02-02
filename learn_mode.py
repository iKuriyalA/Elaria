# learn_mode.py is here

class LearnMode:
    def __init__(self, topic=None):
        self.step = 0
        self.topic = topic
        self.steps = self._build_steps()

    def _build_steps(self):
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
                "expect": None
            }]

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

        steps = [{"prompt": p, "expect": e} for p, e in lessons.get(self.topic, [])]
        steps.append({
            "prompt": f"{self.topic} lesson complete.\nType LEARN to choose another topic.",
            "expect": None
        })
        return steps

    def show_prompt(self):
        print(f"\n[LEARN] {self.steps[self.step]['prompt']}")

    def validate(self, command):
        expected = self.steps[self.step]["expect"]
        if expected is None:
            return True
        if command.strip().upper() == expected:
            self.step += 1
            return True
        print("[LEARN] Follow the instruction exactly.")
        return False

    def finished(self):
        return self.step >= len(self.steps)

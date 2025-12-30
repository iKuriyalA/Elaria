"""
main.py
--------
Program entry point.
Responsible ONLY for:
- starting the CLI loop
- passing user input to Elaria's command engine
"""

import Elaria


def main():
    # Stores all created data structures (array, stack, queue, etc.)
    data_structures = {}

    print("Elaria — Data Structures & Algorithms Visualizer")
    print("Type EXIT to quit.\n")

    running = True
    while running:
        command = input(">>> ")
        running = Elaria.run_command(command, data_structures)


if __name__ == "__main__":
    main()

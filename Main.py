# Program entry point and REPL loop

import Elaria


def main():
    data_structures = {}
    Elaria.show_help()

    while True:
        command = input(">>> ")
        if not Elaria.run_command(command, data_structures):
            break


if __name__ == "__main__":
    main()

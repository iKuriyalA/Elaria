import Elaria as El
def main():
    data_structures = {}
    running = True
    while running:
        command = input(">>> ")
        running = El.run_command(command, data_structures)

if __name__ == "__main__":
    main()

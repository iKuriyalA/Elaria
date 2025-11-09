import Elaria
def main():
    data_structures = {}
    running = True
    while running:
        command = input(">>> ")
        running = Elaria.run_command(command, data_structures)

if __name__ == "__main__":
    main()
# Elaria
Computer language allowing users to build data structures and run algorithms, with the ability to visualize them. Perfect for people learning the in-depth of DSA and for people who  want to learn how to solve complex coding questions.

### How to Setup
To set up you will need to copy the Elaria file and add it into your IDE to transport the language code into your program.
It is recommended to name this as a module called Elaria to be imported later on.

### Adding the Main Command
Import your saved Elaria file:
   
`import Elaria`

Import the build in run command in Elaria and add it to a loop to accomdate to you needs. 

No data structures can be used without a way to place them stored, preferred method: `data_structures = {}`
 ```   
def main():
    data_structures = {}
    running = True
    while running:
        command = input(">>> ")
        running = El.run_command(command, data_structures)
  ``` 
Add the main stream and the program is ready to run: 
 ```
if __name__ == "__main__":
    main()
 ``` 


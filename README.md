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
        running = Elaria.run_command(command, data_structures)
  ``` 
Add the main stream and the program is ready to run: 
 ```
if __name__ == "__main__":
    main()
 ```

# Data Structures
Here are the current data structures used in this language. Following descriptions include how to use them and implement them.

[Arrays](#arrays)

[Stacks](#stacks)

## Arrays
The array structure in the most basic storage unit for data.

The syntax to create an array is: `CREATE ARRAY`

Once you have create an array, you will be able to use the following commands:  

- `ARRAY ADD`: Adds one or more values to the end of the array

- `ARRAY INSERT`: Inserts a value at a specific position

- `ARRAY REMOVE`: Removes one or more values from the array (if they exist)

- `ARRAY DIAGRAM`: Prints the current contents of the array

All values must be inside brackets to avoid logic errors.  
### Example Session  
![image alt](https://github.com/iKuriyalA/Elaria/blob/673f65b93efff9116e077e2d2a1ea3a9cfc4962b/ExArrayRun.png)

## Stacks
The stack structure is a basic model of first-in last-out data storage.

The syntax to create an array is: `CREATE STACK`

Once you have create a stack, you will be able to use the following commands:  

- `STACK PUSH`: Pushes one or more values onto the top of the stack

- `STACK POP`: Removes the top item from the stack

- `STACK DIAGRAM`: Displays the stack visually (top to bottom)

All values must be inside brackets to avoid logic errors.  
### Example Session 
![image alt](https://github.com/iKuriyalA/Elaria/blob/673f65b93efff9116e077e2d2a1ea3a9cfc4962b/ExStackRun.png)

# Algorithms
Here are the current algorithms used in this language. Following descriptions include how to use them and implement them.  

## SearchAlgorithms
Algorithms designed to locate a specific value from data using a specific method and path.

### Linear Search
### Binary Search
### Depth First Search
### Breadth First Search

*This project has been created as part of the 42 curriculum by nel-ouad.*

## Description

**push_swap** is a sorting algorithm project that consists of sorting a stack of integers using a limited set of operations.  
The goal is to sort the numbers in ascending order while minimizing the number of instructions printed to standard output.

This project implements **only the mandatory part** of push_swap.

## Instructions

### Compilation

make

### Execution

./push_swap \<number1\> \<number2\> ... \<numberN\>

The program accepts any valid integer input and outputs the list of operations required to sort the stack.

## Algorithm

The sorting strategy is based on **indexing values and grouping them into chunks**, allowing efficient transfers between stacks and reducing the total number of operations.  
The approach adapts depending on the size of the input.

## Resources

- 42 push_swap subject

### AI Usage

ChatGPT was used for optimization ideas and inspiration, particularly to explore common strategies and ways to reduce the number of operations.

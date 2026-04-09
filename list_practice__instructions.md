## Setup
1. You know the drill.
2. Call the file `list_practice.py`

## Instructions

### Task 1
Make a program in a function called rolled_dice() -> float that does the following:
- Keep rolling dice and print the dice number until a 6 is rolled. Hint: use rand.int. and a while loop
- Stores all the dice rolls in a list
- Calculate and returns the average of the dice roll, rounded to one decimal place. Hint: use sum() and len()

#### Sample Output:
```plaintext
Welcome to the Dice Rolling Game!
You rolled a: 5
You rolled a: 1
You rolled a: 6
Average dice roll: 4.0
```

### Task 2
Write a program to figure out how popular the name "john" is.
- Ask the user for some names, using a `while` loop, while the name is not blank. 
- Store each inputted name into a list called `names`. 
- Create a function called count_john(names:list[str]) -> float that figure out what percentage of names entered are "john" by counting the number of "john"s in the list, dividing it by the total number of names in the list, then multiplying that result by 100.Return that value to use in main()
- Once you have the percentage, print the following message: f"{percentage}% of the names are john"

#### Sample Output

```plaintext
Enter a name (or blank to stop): mark
Enter a name (or blank to stop): john
Enter a name (or blank to stop): henry
Enter a name (or blank to stop): john
Enter a name (or blank to stop): john
Enter a name (or blank to stop): barbara
Enter a name (or blank to stop):
50.0% of the names are john  
```

### Starter code
```python
"""
author:
date:
Practicing with lists
"""

def roll_dice() -> int:
    """
    TODO: write docstring
    """

def count_john(names: list[str]) -> float:
    """
    Returns the percentage of names that are "john" in the list.

    Args:
        names (list[str]): the list of names that were inputted by user in main()
    
    Returns:
        float: the percentage of names that were "john" in names, rounded to one decimal place
    
    Example:
    >>> count_john(["sara", "abc", "john"])
    33.3
    """
    # TODO: implement this function

def main():
    """
    Program to run the two tasks.
    """
    # Input - initialize empty list to add names
    names = []

    # Processing
    # TODO: call dice_roll() function and store the value into a variable
    name = input("Enter a name (or blank to stop): ").lower()
    # TODO: get user input names and add them to names
    # TODO: call count_john(names) function and store the value into a variable

    # Output
    # TODO: print the dice average and john average
```
# Minimum Operations Calculator

This project contains a Python solution that calculates the minimum number of operations required to achieve a target number of 'H' characters in a text file, given only two available operations: Copy All and Paste.

## Problem Description

In a text editor, you have a single character 'H'. The editor allows only two operations:
1. Copy All: Copies all current characters
2. Paste: Pastes the characters from the last Copy All operation

Given a number `n`, the task is to calculate the fewest number of operations needed to get exactly `n` 'H' characters in the file.

## Function Description

The solution is implemented in the [`minOperations`](0-minoperations.py) function:

```python
def minOperations(n):
    """
    Calculates the fewest number of operations needed to get n H characters
    
    Args:
        n: target number of H characters
        
    Returns:
        Integer: minimum number of operations
        Returns 0 if n is impossible to achieve
    """
```

### Parameters
- `n` (integer): The target number of 'H' characters to achieve

### Return Value
- Returns an integer representing the minimum number of operations required
- Returns 0 if n ≤ 1 (impossible or no operations needed)

## Algorithm

The solution uses a prime factorization approach:
1. If n ≤ 1, return 0 (no operations needed)
2. For each possible divisor starting from 2:
   - While n is divisible by the current divisor:
     - Add the divisor to the total operations count
     - Divide n by the divisor
   - If no more divisors are found and n > 1, add n to operations (n is prime)

## Examples

```python
minOperations(4)  # Returns: 4 (Copy All -> Paste -> Copy All -> Paste)
minOperations(12) # Returns: 8
minOperations(1)  # Returns: 0
```

## Usage

```python
from minoperations import minOperations

result = minOperations(9)
print(result)  # Output: 6
```

## Time Complexity
- O(sqrt(n)) in the worst case, where n is the input number

## Space Complexity
- O(1) as it uses only a constant amount of extra space

## Requirements
- Python 3.x
- No external libraries required
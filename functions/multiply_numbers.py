# Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

import functools
import sys

def multiply_numbers(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

def main():
    args = sys.argv[1:]
    if not args:
        nums = input('Please enter any numbers you\'d like to get the absolute value of: ').split(' ')
    else:
        nums = args
    nums = [int(n) for n in nums]
    print(multiply_numbers(nums))

if __name__ == '__main__':
    main()

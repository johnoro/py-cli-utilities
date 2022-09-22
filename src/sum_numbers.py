# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

import sys

def sum_numbers(numbers):
    return sum(numbers)

def main():
    args = sys.argv[1:]
    if not args:
        numbers = input('Please enter a list of numbers separated by spaces: ').split(' ')
        if len(numbers) == 1 and numbers[0] == '':
            numbers = []
    else:
        numbers = args
    
    numbers = [int(n) for n in numbers]
    print(sum_numbers(numbers))

if __name__ == '__main__':
    main()

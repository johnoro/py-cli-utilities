# - Largest among three number
# Write a Python function to find the Max of three numbers.

import sys

def max_of_three(a, b, c):
    return max(a, b, c)

def main():
    args = sys.argv[1:]
    if not args:
        nums = input('Please enter three numbers separated by spaces: ').split(' ')
    else:
        nums = args
    
    nums = [int(n) for n in nums]
    print(max_of_three(*nums))

if __name__ == '__main__':
    main()

# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

import functools
import sys

def reverse_string(string):
    return functools.reduce(lambda x, y: y + x, string)

def main():
    args = sys.argv[1:]
    if not args:
        string = input('Please enter a string you\'d like to reverse: ')
    else:
        string = args[0]

    print(reverse_string(string))

if __name__ == '__main__':
    main()

# Write a Python program to check a list is empty or not.

import sys

def is_empty(elements):
    return not elements

def main():
    args = sys.argv[1:]
    if not args:
        elements = input('Please enter a list of elements separated by spaces: ').split(' ')
        if len(elements) == 1 and elements[0] == '':
            elements = []
    else:
        elements = args
    
    print(is_empty(elements))

if __name__ == '__main__':
    main()

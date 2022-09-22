# Write a Python program to remove duplicates from a list.

import sys

def remove_duplicates(elements):
    return list(set(elements))

def main():
    args = sys.argv[1:]
    if not args:
        elements = input('Please enter a list of elements separated by spaces: ').split(' ')
        if len(elements) == 1 and elements[0] == '':
            elements = []
    else:
        elements = args
    
    print(remove_duplicates(elements))

if __name__ == '__main__':
    main()

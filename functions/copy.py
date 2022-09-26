# Write a Python program to clone or copy a list

import sys

def clone_list(elements):
    cloned = []
    for l in elements:
        if type(l) == list:
            cloned.extend(clone_list(l))
        else:
            cloned.append(l)
    return cloned

def main():
    args = sys.argv[1:]
    if not args:
        elements = input('Please enter a list of elements separated by spaces: ').split(' ')
    else:
        elements = args
    print(clone_list(elements))

if __name__ == '__main__':
    main()

# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

import sys

def count_same_first_last(strings):
    return len([s for s in strings if len(s) > 1 and s[0] == s[-1]])

def main():
    args = sys.argv[1:]
    if not args:
        strings = input('Please enter a list of strings separated by spaces: ').split(' ')
        if len(strings) == 1 and strings[0] == '':
            strings = []
    else:
        strings = args
    
    print(count_same_first_last(strings))

if __name__ == '__main__':
    main()

# - Absolute value using function

import sys

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

def main():
    args = sys.argv[1:]
    if not args:
        nums = input('Please enter any numbers you\'d like to get the absolute value of: ').split(' ')
    else:
        nums = args
        
    for n in nums:
        print(absolute_value(int(n)))

if __name__ == '__main__':
    main()


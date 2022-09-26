# - Check Prime Number

import sys

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    args = sys.argv[1:]
    if not args:
        elements = input('Please enter any numbers you\'d like to check: ').split(' ')
    else:
        elements = args
    
    for num in elements:
        if is_prime(int(num)):
            print(f'{num} is a prime number.')
        else:
            print(f'{num} is not a prime number.')

if __name__ == '__main__':
    main()

# - Generate Fibonacci Sequence

import sys

f_cache = {0:0, 1:1}

def fibonnaci(n, memo=f_cache):
    if n not in memo:
        memo[n] = fibonnaci(n-1, memo) + fibonnaci(n-2, memo)
    return memo[n]

def main():
    args = sys.argv[1:]
    if not args:
        elements = input('Please enter any numbers you\'d like to generate the fibonnaci sequence for: ').split(' ')
    else:
        elements = args
    
    for num in elements:
        print(num, ': ', fibonnaci(int(num)))

if __name__ == '__main__':
    main()

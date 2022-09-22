# - Leap Year

import sys

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

def main():
    args = sys.argv[1:]
    if not args:
        years = input('Please enter any years you\'d like to check: ').split(' ')
    else:
        years = args
    
    for year in years:
        is_not = '' if is_leap_year(int(year)) else 'not '
        print(f'{year} is {is_not}a leap year')
        
if __name__ == '__main__':
    main()

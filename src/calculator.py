# - Simple Calculator
# to add proper order of operations, 
# a stack could be used 
# along with some priority rules stored with each operator
# (plus a rule to read parentheses)

import sys

ops = { 
    'add': '+', 
    'subtract': '-', 
    'multiply': '*', 
    'divide': '/', 
    'power': '^'
}

def calc(operand1, operator, operand2):
    if operator == ops['add']:
        return operand1 + operand2
    if operator == ops['subtract']:
        return operand1 - operand2
    if operator == ops['multiply']:
        return operand1 * operand2
    if operator == ops['divide']:
        return operand1 / operand2
    if operator == ops['power']:
        return operand1 ** operand2
    print("Invalid operator; current operators are: " + ", ".join(ops.values()))

def calc_helper(eq_it, total):
    while True:
        try:
            op = next(eq_it)
            operand = int(next(eq_it))
            total = calc(total, op, operand)
        except:
            return total

def main():
    args = sys.argv[1:]
    print('Please type your equation with spaces in between each operator and operand.\n' + f'Please note that operations are executed in the order they come and that parentheses are not supported.')
    if not args:
        args = input('Please enter your equation: ').split(' ')
    eq_it = iter(args)
    total = int(next(eq_it))

    total = calc_helper(eq_it, total)
    print(total)

if __name__ == '__main__':
    main()

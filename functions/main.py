# acts as a gateway to all other functions

import sys
import os

def main():
    args = sys.argv[1:]
    src_dir = 'functions'
    dirs = os.listdir(src_dir)
    functions = [f.removesuffix('.py') for f in dirs]
    functions.remove('main')
    functions_str = ', '.join(functions)
    print(f'\nCurrently available functions: {functions_str}')

    while True:
        if not args:
            try:
                args = input('\nPlease enter a function name, with any arguments after it with spaces in between: ').split(' ')
            except KeyboardInterrupt:
                print('Exiting...')
                sys.exit()
        func = args[0]
        if func in functions:
            try:
                os.system(f'python {src_dir}/{func}.py {" ".join(args[1:]) if len(args) > 1 else ""}')
            except KeyboardInterrupt:
                print('Exiting...')
                sys.exit()
            except:
                print('Error running function')
        else:
            print(f'Function {func} not found.')
            print(f'Available functions: {functions_str}')
        args = []

if __name__ == '__main__':
    main()

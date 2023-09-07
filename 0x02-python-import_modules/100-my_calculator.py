#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    ac = len(argv)

    if ac < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = str(argv[2])

    ops = ['+', '-', '*', '/']

    if op == ops[0]:
        ans = add(a, b)

    elif op == ops[1]:
        ans = sub(a, b)

    elif op == ops[2]:
        ans = mul(a, b)

    elif op == ops[3]:
        ans = div(a, b)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {op} {b} = {ans}")

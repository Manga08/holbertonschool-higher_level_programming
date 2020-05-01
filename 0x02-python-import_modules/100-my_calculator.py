#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if(len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(argv[1])
    op = argv[2]
    n2 = int(argv[3])
    if(op == "+"):
        print("{} + {} = {}".format(n1, n2, add(n1, n2)))
    elif(op == "/"):
        print("{} / {} = {}".format(n1, n2, div(n1, n2)))
    elif(op == "-"):
        print("{} - {} = {}".format(n1, n2, sub(n1, n2)))
    elif(op == "*"):
        print("{} * {} = {}".format(n1, n2, mul(n1, n2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

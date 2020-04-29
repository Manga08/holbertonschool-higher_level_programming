#!/usr/bin/python3
def fizzbuzz():
    for fb in range(1, 101):
        if fb % 15 == 0:
            print("FizzBuzz", end=' ')
        elif fb % 5 == 0:
            print("Buzz", end=' ')
        elif fb % 3 == 0:
            print("Fizz", end=' ')
        else:
            print(fb, end=' ')

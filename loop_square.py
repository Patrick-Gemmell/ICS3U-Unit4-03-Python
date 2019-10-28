#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: OcTober 2019
# This program adds up a loop counter


def main():
    # This function adds up a loop counter
    integer = input("Enter an integer: ")
    loop_counter = 0
    total = 0
    # inputs
    try:
        integer_as_number = int(integer)
        for loop_counter in range(integer_as_number):
            print("")
            total = loop_counter**2
            print("{0}^2 = {1}".format(loop_counter, total))
        print("")
    except Exception:
        print("that is not an integer")


if __name__ == "__main__":
    main()

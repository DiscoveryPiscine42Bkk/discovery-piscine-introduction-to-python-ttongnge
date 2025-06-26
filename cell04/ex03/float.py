#!/usr/bin/env python3

num = input("Give me a number: ")


if '.' in num:
    
    integer_part, decimal_part = num.split('.')
    # Check if decimal part has non-zero digits
    if any(digit != '0' for digit in decimal_part):
        print("This number is a decimal.")
    else:
        print("This number is an integer.")
else:
    print("This number is an integer.")
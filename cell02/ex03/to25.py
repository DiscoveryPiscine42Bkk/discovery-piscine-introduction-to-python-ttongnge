#!/usr/bin/env python3

start = int(input("Enter a number less than 25\n"))

if start > 25:
    print("Error")
else:
    while start <= 25:
        print(f"Inside the loop, my variable is {start}")
        start += 1
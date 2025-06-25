#!/usr/bin/env python3

Test01 = int(input("Enter the first number:\n"))
Test02 = int(input("Enter the second number:\n"))

result = Test01 * Test02

print(f"{Test01} x {Test02} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
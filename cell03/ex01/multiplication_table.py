#!/usr/bin/env python3

def main():
    try:
        number = int(input("Enter a number\n"))
        for i in range(10):
            print(f"{i} x {number} = {i * number}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

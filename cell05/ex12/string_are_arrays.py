#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print("none")
    else:
        input_string = sys.argv[1]
        z_count = input_string.count('z')
        if z_count == 0:
            print("none")
        else:
            print('z' * z_count)

if __name__ == "__main__":
    main()
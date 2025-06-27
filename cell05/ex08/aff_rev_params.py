#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        # Print arguments in reverse order (excluding script name)
        for arg in reversed(sys.argv[1:]):
            print(arg)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 3:
        print("none")
    else:
        keyword = sys.argv[1]
        text = sys.argv[2]
        count = text.count(keyword)
        print(count if count > 0 else "none")

if __name__ == "__main__":
    main()
    
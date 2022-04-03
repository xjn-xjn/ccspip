# TODO: write fib3.py

from typing import Dict

# establish base case in a dictionary
# using key value pairs
memo: Dict[int, int] = {0:0, 1:1}

if __name__ == "__main__":
    print("key: 0, val: " + str(memo[0]))
    print("key: 1, val: " + str(memo[1]))

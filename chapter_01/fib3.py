# TODO: write fib3.py

from typing import Dict

# establish base case in a dictionary
# using key value pairs
memo: Dict[int, int] = {0:0, 1:1}

def fib3(y):
    if y not in memo:
        memo[y] = fib3(y-1) + fib3(y-2)

    return memo[y]



if __name__ == "__main__":
    print(fib3(50))
    print("able to calculate fibonacci(50) ^ using memorization technique")

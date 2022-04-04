# TODO: write fib3.py

from typing import Dict

# establish base case in a dictionary
# using key value pairs
memo: Dict[int, int] = {0:0, 1:1}

def fib3(y: int) -> int:
    if y not in memo:
        memo[y] = fib3(y-1) + fib3(y-2)

    return memo[y]



if __name__ == "__main__":
    n_start = 0
    n_stop = 150
    
    print("the fibonacci sequence to " + str(n_stop))
    for i in range(n_start, n_stop):
        print(fib3(i))

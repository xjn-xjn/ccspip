def fib2(x):
    # establish base case to prevent infinite recursion
    if x < 2:
        return x
    return fib2(x-1) + fib2(x-2)


if __name__ == "__main__":
    print(fib2(25))
    print("fib2.py finished running")

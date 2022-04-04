from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(b):  # same def as fib 2
    if b < 2:
        return b
    return fib4(b-1) + fib4(b-2)

if __name__ == "__main__":
    print(fib4(150))

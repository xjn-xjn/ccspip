# TODO: write fib 5

def fib5(n: int) -> int:
    if n == 0:  return n # special case
    lastn: int = 0
    nextn: int = 1

    for _ in range(1, n):
        lastn, nextn = nextn, lastn + nextn
    return nextn


if __name__ == "__main__":
    print("fib5")
    print(fib5(50))

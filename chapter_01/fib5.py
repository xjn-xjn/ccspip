# TODO: write fib 5

def fib5(n):
    if n == 0:  return n # special case
    lastn = 0
    nextn = 1

    for _ in range(1, n):
        lastn, nextn = nextn, lastn + nextn
    return nextn


if __name__ == "__main__":
    print("fib5")
<<<<<<< Updated upstream
    print(fib5(50))
=======
    print("hello from Acode")
>>>>>>> Stashed changes

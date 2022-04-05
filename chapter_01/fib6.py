from typing import Generator

def fib6(n) -> Generator [int, None, None]:
  yield 0
  
# TODO : vonvert fib 5 to generator
  
if __name__ == "__main__":
  print(fib6(50))
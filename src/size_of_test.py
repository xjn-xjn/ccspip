def make_array(j: int, k: int) -> list:
  """ Creates an incremented array of size j, k.
  Args:
    j: int -> number of rows
    k: int -> number of columns
  Returns
    an list of lists representing an array is returned consisting of 0 through max number array can hold.
  """
  
  return [j, k]
  
  
if __name__ == "__main__":
  my_array = make_array(1, 2)
  print(my_array)
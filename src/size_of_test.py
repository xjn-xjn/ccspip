def make_array(j: int, k: int) -> list:
  """ Creates an incremented array of size j, k.
  Args:
    j: int -> number of rows
    k: int -> number of columns
  Returns
    an list of lists representing an array is returned consisting of 0 through max number array can hold.
  """
  
  element = 0  # our initial array element
  array = []
  # loop through rows
  for row in range(j):
    # new row
    new_row = []
    # loop through columns
    for col in range(k):
      # append element to row
      new_row.append(element)
      # increment elemwnt
      element += 1
    # append row to array
    array.append(new_row)
      
    
  
  return array
  
  
if __name__ == "__main__":
  my_array = make_array(1, 2)
  print(my_array)
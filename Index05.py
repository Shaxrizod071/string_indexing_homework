def main(a):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
   i=0
   if a[0].isdigit():
      i+=1
   if a[1].isdigit():
      i+=1
   if a[2].isdigit():
      i+=1
   if a[3].isdigit():
      i+=1
   if a[4].isdigit():
      i+=1
    return i
print(main('ef42k'))

def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if len(s)<=5:
        return len(s)*('*')
    if len(s)>5:
        return False
    else:
        return False
print(main('salom'))
        

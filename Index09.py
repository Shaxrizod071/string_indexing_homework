def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if len(s)<=9 and s==int:
        return s
    else:
        return -1
print(main('12'))

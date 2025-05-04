def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=''
    for i in s:
        a+=i
    return '+'.join(a)
print('1','2','3')

def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a%10
    y = a//10
    z = y%10
    e = y//10
    return (x+z+e)%2==1
print(main(247))
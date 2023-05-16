def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    # ?????
    
    a = x%10
    x = x//10
    c = x%10
    x = x//10
    if a==c:
        return True
print(main(33))


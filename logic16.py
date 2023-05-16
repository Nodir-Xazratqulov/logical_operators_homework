def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer

    """
    # 13425
    # x = a%10
    # y = a//10
    # z = y%10
    # e = y//10
    # b = e%10
    # d = e//10
    # f = d%10
    # g = d//10
    #  x,z,b,f,g   mnatematik aperatorlar bn ishlash
    return 10000 <= a and a <= 99999
print(main(13465))
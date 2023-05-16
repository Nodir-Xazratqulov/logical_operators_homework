def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a%10 #4
    a = a//10 
    z = a%10 #3
    a = a//10
    b = a%10#2
    a = a//10
    f = a%10#1
    a = a//10#0   #1 2 3 4 5
    #  x,z,b,f,g  #0 1 2 3 4

    k = 0 #counter
    if x<z and z<b and b<f and f<a:
        k += 1
        return True
    if k==0:
        return False
print(main(76943))
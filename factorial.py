def fact(n):
    """
    Calculate n!
    """
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        return n * fact(n - 1)

print(fact(5))
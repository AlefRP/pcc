# Fibonacci using memoization
m = dict()

def fib_mem(n):
    """
    Fibonacci using memoization
    :param n: Number to find fibonacci of
    :return: Fibonacci of n
    """
    if n < 2:
        return n
    if m.get(n):
        return m[n]
    else:
        m[n] = fib_mem(n-1) + fib_mem(n-2)
        return m[n]

print(fib_mem(10))
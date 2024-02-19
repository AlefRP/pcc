import time

def fib_rec(n):
    """
    Calculate fibonacci number
    """
    if n < 0:
        raise ValueError("n must be positive")
    
    # base cases 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    """
    Calculate fibonacci number
    """
    res = n
    a, b = 0, 1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
    return res

n = 20

# Medindo o tempo para a versão recursiva
start = time.time()
result_rec = fib_rec(n)
elapsed_rec = time.time() - start
print(f"{result_rec}")
print(f"Recursive time: {elapsed_rec:.20e} seconds")  # Usando notação científica com precisão

# Medindo o tempo para a versão iterativa
start = time.time()
result_iter = fib_iter(n)
elapsed_iter = time.time() - start
print(f"{result_iter}")
print(f"Iterative time: {elapsed_iter:.20e} seconds")
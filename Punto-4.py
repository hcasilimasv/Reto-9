import time
def fibonacci_it(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def fibonacci_re(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_re(n - 1) + fibonacci_re(n - 2)
n = int(input("Ingrese el número de la serie de Fibonacci que desea calcular: "))
start_time = time.time()
fib_iter_result = fibonacci_it(n)
end_time = time.time()
iterative_timer = end_time - start_time
print("Tiempo en ejecutar (iterativo):", iterative_timer)
start_time = time.time()
fib_rec_result = fibonacci_re(n)
end_time = time.time()
recursive_timer = end_time - start_time
print("Tiempo en ejecutar (recursivo):", recursive_timer)
print("Fibonacci resultado (iterativo):", fib_iter_result)
print("Fibonacci resultado (recursivo):", fib_rec_result)
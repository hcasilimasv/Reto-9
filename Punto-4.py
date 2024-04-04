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
start_time = time.time()
fib_iter_result = fibonacci_it(30)
end_time = time.time()
iterative_timer = end_time - start_time
print("Tiempo en ejecutar en segundos (iterativo):", iterative_timer)
print("Fibonacci resultado (iterativo):", fib_iter_result)
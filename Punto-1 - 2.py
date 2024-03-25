factorial = (lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))(lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))
n = int(input("Escriba un numero natural para calcular el factorial"))
if n >= 0:
    fact = factorial(n)
    print("El factorial de " + str(n) + " es: " + str(fact))
else:
    print("Los numeros negativos no tienen factorial. Por favor, escriba un numero entero positivo")
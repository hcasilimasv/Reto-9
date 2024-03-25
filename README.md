# Reto-9

#### 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

##### 1.
```python
cuad = lambda x: x ** 2
for i in range(1, 101):
    print(f"Numero: {i}, Cuadrado: {cuad(i)}")
```

##### 2.

``` python
factorial = (lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))(lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))
n = int(input("Escriba un numero natural para calcular el factorial"))
if n >= 0:
    fact = factorial(n)
    print("El factorial de " + str(n) + " es: " + str(fact))
else:
    print("Los numeros negativos no tienen factorial. Por favor, escriba un numero entero positivo")
```

##### 3.
``` pyrhon
impr_div = lambda n: print("Los divisores de " + str(n) + " son:\n" + "\n".join(str(div) for div in range(1, n + 1) if n % div == 0)) if 2 <= n <= 50 else print("El numero escrito no está dentro del rango")
n = int(input("Escriba un numero entre 2 y 50: "))
impr_div(n)
```



#### 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

##### 1.
``` python
def impr_cuad(*args):
    for n in args:
        print("Numero " + str(n) + " , Cuadrado = " + str(n * n))
impr_cuad(*range(1, 101))
```

##### 2.
``` python
def cal_fact(*args):
    for n in args:
        if n >= 0:
            fact = 1
            cont = n
            while cont > 0:
                fact *= cont
                cont -= 1
            print("El factorial de " + str(n) + " es: " + str(fact))
        else:
            print("Los numeros negativos no tienen factorial, escriba un entero positivo")
num = [int(input("Escriba un numero natural para calcular el factorial"))]
cal_fact(*num)
```

##### 3.
``` python
def pot(x, n):
    exp = 1
    for _ in range(n):
        exp *= x
    return exp
cal_pot = lambda *args: pot(*args)
x = float(input("Escriba un numero real"))
n = int(input("Escriba un numero natural"))
resultado = cal_pot(x, n)
print("El resultado de " + str(x) + " elevado a " + str(n) + " es " + str(resultado))
```


#### 3. Escriba una función recursiva para calcular la operación de la potencia.

``` python
def pot(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * pot(x, n - 1)
    else:
        return 1 / pot(x, -n)
bas = float(input("Escriba la base del numero "))
exp = int(input("Escriba el exponente del numero"))
resul = pot(bas, exp)
print(f"{bas} elevado a la {exp} es igual a {resul}")
```



#### 4. Utilice la siguiente plantilla de code para contar el tiempo:
```
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
##### Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.

``` python
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
```



#### 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo

[![Captura7.png](https://i.postimg.cc/05dnCjJQ/Captura7.png)](https://postimg.cc/V5vXfYgQ)



#### 6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

##### Mi perfil
https://www.linkedin.com/in/hernan-javier-casilimas-vega-77647a300/


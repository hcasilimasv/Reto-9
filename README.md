# Reto-9

#### 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

##### 1.
```python
#Definimos la funcion con lambda
cuad = lambda x: x ** 2
#Itineramos la funcion
for i in range(1, 101):
    print(f"Numero: {i}, Cuadrado: {cuad(i)}")
```

##### 2.

``` python
#Definimos la función factorial usando una expresión lambda recursiva
factorial = (lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))(lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))

# Solicitamos al usuario que ingrese un número natural para calcular su factorial
n = int(input("Escriba un numero natural para calcular el factorial"))

#Verificamos si el número ingresado es no negativo
if n >= 0:
    fact = factorial(n)
    print("El factorial de " + str(n) + " es: " + str(fact))
else:
    print("Los numeros negativos no tienen factorial. Por favor, escriba un numero entero positivo")
```

##### 3.
``` pyrhon
#Definimos una función lambda para imprimir los divisores de un número dado
impr_div = lambda n: print("Los divisores de " + str(n) + " son:\n" + "\n".join(str(div) for div in range(1, n + 1) if n % div == 0)) if 2 <= n <= 50 else print("El numero escrito no está dentro del rango")

#Solicitamos al usuario que ingrese un número entre 2 y 50
n = int(input("Escriba un numero entre 2 y 50: "))
impr_div(n)
```



#### 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

##### 1.
``` python
#Definimos la función para imprimir el cuadrado de los números pasados como argumentos
def impr_cuad(*args):
    for n in args:
        print("Numero " + str(n) + " , Cuadrado = " + str(n * n))

#Se llama a la función impr_cuad con una secuencia de números del 1 al 100
impr_cuad(*range(1, 101))
```

##### 2.
``` python
#Definimos una función para calcular el factorial de los números pasados como argumentos
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

#Se solicita al usuario que ingrese un número natural para calcular su factorial
num = [int(input("Escriba un numero natural para calcular el factorial"))]

#Llamos a la funcion
cal_fact(*num)
```

##### 3.
``` python
#Definimos una función para calcular la potencia de un número
def pot(x, n):
    exp = 1
    for _ in range(n):
        exp *= x
    return exp

#Definimos una función lambda que llama a la función pot
cal_pot = lambda *args: pot(*args)

#Solicitamos al usuario que escriba
x = float(input("Escriba un numero real"))
n = int(input("Escriba un numero natural"))

#Se calcula el resultado de x elevado a n utilizando la función cal_pot e imprimimos
resultado = cal_pot(x, n)
print("El resultado de " + str(x) + " elevado a " + str(n) + " es " + str(resultado))
```


#### 3. Escriba una función recursiva para calcular la operación de la potencia.

``` python
#Definimos una función para calcular la potencia de un número
def pot(x, n):

#Tenemos un caso base: cualquier número elevado a 0 es 1
    if n == 0:
        return 1

#Tenemos un caso positivo: x elevado a un exponente positivo
    elif n > 0:
        return x * pot(x, n - 1)

#Tenemos un caso negativo: x elevado a un exponente negativo
    else:
        return 1 / pot(x, -n)

#Se solicita al usario que escriba
bas = float(input("Escriba la base del numero "))
exp = int(input("Escriba el exponente del numero"))

#Se calcula el resultado de la potencia utilizando la función pot e imprimimos
resul = pot(bas, exp)
print(f"{bas} elevado a la {exp} es igual a {resul}")
```



#### 4. Utilice la siguiente plantilla de code para contar el tiempo:
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

#### Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa


``` python
import time

#Definimos fibonacci
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

#aplicamos la plantilla de code para contar el tiempo
start_time = time.time()

#En esta parte podemos cambiar el valor del número de fibonacci que queremos calcular y contar
fib_iter_result = fibonacci_it(30) 
end_time = time.time()
iterative_timer = end_time - start_time

#Imprimimos
print("Tiempo en ejecutar en segundos (iterativo):", iterative_timer)
print("Fibonacci resultado (iterativo):", fib_iter_result)
```

[![Captura12.png](https://i.postimg.cc/N0Q7cZLz/Captura12.png)](https://postimg.cc/Mnrj0P77)
##### A partir del número 2.000.000 el tiempo se vuelve significativo, porque si ponemos un número mayor a este, el tiempo de cálculo que genera el código se amplía.

#### 5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo

[![Captura7.png](https://i.postimg.cc/05dnCjJQ/Captura7.png)](https://postimg.cc/V5vXfYgQ)



#### 6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

##### Mi perfil
https://www.linkedin.com/in/hernan-javier-casilimas-vega-77647a300/


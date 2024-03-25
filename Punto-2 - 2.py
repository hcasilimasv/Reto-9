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
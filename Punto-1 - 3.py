impr_div = lambda n: print("Los divisores de " + str(n) + " son:\n" + "\n".join(str(div) for div in range(1, n + 1) if n % div == 0)) if 2 <= n <= 50 else print("El numero escrito no está dentro del rango")
n = int(input("Escriba un numero entre 2 y 50: "))
impr_div(n)
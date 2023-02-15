n1 = int(input("Ingrese el rango inicial: "))
n2 = int(input("Ingrese el rango final: "))

primos = []

for num in range(n1, n2 + 1 ):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            primos.append(num)
print(primos)


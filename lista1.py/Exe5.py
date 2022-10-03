cont = 0
soma = 0

for i in range(0,20):
    x = int(input("Digite um valor: "))
    if x % 2 == 0:
        cont += 1
        soma += x
print("A media e: ", (soma/cont))

entrada = int(input("Digite um valor: "))

def fatorial(valor):
    fat = 1
    for i in range(2,valor+1):
        fat = fat*i
    return fat

def tabuada(valor):
    for i in range(1,11):
        print(f"{i}  X  {valor}  =  {valor*i}")


if entrada%2==0:
    print(f"O fatorial de {entrada} é: {fatorial(entrada)}")
else:
    tabuada(entrada)
    
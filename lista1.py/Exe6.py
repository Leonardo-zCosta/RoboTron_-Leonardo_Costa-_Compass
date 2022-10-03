valor = int(input("Digite um valor: "))

if(valor < 2):
     print("Digite um valor maior que 2")
else:
    for x in range(0, valor):
        if (x % 2 != 0):
            print(x)
    

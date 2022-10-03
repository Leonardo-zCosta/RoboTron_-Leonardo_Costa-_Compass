cont = 0
frutas = ["maça", "banana", "pera"]
frutasCopy = frutas.copy()
listaDeFrutas = []

for i in range(0,3):
    listaDeFrutas.append(input())

for fruta in range(0,3):
    if frutas[fruta] in listaDeFrutas: 
        cont += 1
        

print(f"A lista de frutas lidas possui {cont} frutas iguais a lista original")
print("Lista de frutas lidas: ", listaDeFrutas)
print("Lista de frutas original: " ,frutasCopy)


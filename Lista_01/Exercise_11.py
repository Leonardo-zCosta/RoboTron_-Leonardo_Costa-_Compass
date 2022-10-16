
inicial = int(input("Hora de inicio:")) 
final= int(input("Hora de termino:"))

if inicial < final:
    tempo = final - inicial
else:
    tempo = (24 - inicial) + final
print(f'O JOGO DUROU {tempo} HORA(S)')


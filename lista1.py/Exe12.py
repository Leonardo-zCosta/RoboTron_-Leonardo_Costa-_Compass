from tkinter import dialog


idade = int(input("Digite a idade: "))

ano=int(idade/365); 

mes=int((idade%365)/30)

dia=int((idade%365)%30)

print(ano, " ano(s)")
print(mes, " mes(es)")
print(dia, " dia(s)")
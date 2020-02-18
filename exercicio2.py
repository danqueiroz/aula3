lista = {
        1:'domingo',
        2:'segunda',
        3:'terça',
        4:'quarta',
        5:'quinta',
        6:'sexta',
        7:'sábado'}

repetir = "Sim"

num_dia = int(input("Digite um número de 1 a 7: "))

if num_dia > 7 and num_dia:
    repetir = input("O número não é válido!")
else:
    print("O dia da semana é", lista.get(num_dia))
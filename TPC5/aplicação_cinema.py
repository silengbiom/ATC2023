import os
import msvcrt as m


def inserir_sala(cinema, sala):
    cinema.append(sala)
    print(f"Sala {len(cinema)} adicionada com sucesso")


def remover_sala(cinema, sala):
    if sala in cinema:
        cinema.remove(sala)
        print(f"Sala removida com sucesso")
    else:
        print("Sala não encontrada")


def listar(cinema):
    for sala in cinema:
        print(f"Sala:{cinema.index(sala) + 1} | Lotação {sala[0]} | Filme: {sala[2]}")


def disponivel(cinema, filme, lugar):
    for sala in cinema:
        if sala[2] == filme and lugar not in sala[1]:
            return f"Lugar {lugar} disponível na Sala {cinema.index(sala) + 1}"
    return "Lugar não disponível"


def vende_bilhete(cinema, filme, lugar):
    for sala in cinema:
        if sala[2] == filme and lugar not in sala[1]:
            sala[1].append(lugar)
            return f"Bilhete vendido para o Lugar {lugar} na Sala {cinema.index(sala) + 1}"
    return "Não foi possível vender o bilhete"


def listar_disponibilidades(cinema):
    for sala in cinema:
        disponiveis = sala[0] - len(sala[1])
        print(f"Sala {cinema.index(sala) + 1}: {disponiveis} lugares disponíveis")


def tecla_para_continuar():
    print("\n\nPressione qualquer tecla para continuar")
    m.getch()
    


cinema = []
escolha = 1
while (escolha != 0):
    os.system('cls')
    print("Menu:\n")
    print("1 -> Listar")
    print("2 -> Disponível")
    print("3 -> Vende bilhete")
    print("4 -> Listar disponibilidades")
    print("5 -> Inserir sala")
    print("6 -> Remover sala")
    print("0 -> Sair")

    escolha = input("\nEscolha uma opção: ")
    os.system('cls')

    if escolha == "1":
        listar(cinema)

    elif escolha == "2":
        filme = input("Nome do filme: ")
        lugar = int(input("Número do lugar: "))
        print(disponivel(cinema, filme, lugar))

    elif escolha == "3":
        filme = input("Nome do filme: ")
        lugar = int(input("Número do lugar: "))
        print(vende_bilhete(cinema, filme, lugar))

    elif escolha == "4":
        listar_disponibilidades(cinema)

    elif escolha == "5":
        nlugares = int(input("Lotação da sala: "))
        vendidos = []
        filme = input("Nome do filme: ")
        sala = [nlugares, vendidos, filme]
        inserir_sala(cinema, sala)

    elif escolha == "6":
        sala = int(input("Número da sala a ser removida: ")) - 1
        if 0 <= sala < len(cinema):
            remover_sala(cinema, cinema[sala])
        else:
            print("Sala não encontrada")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
tecla_para_continuar()
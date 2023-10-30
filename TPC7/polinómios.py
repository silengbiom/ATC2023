import matplotlib.pyplot as plt

polinomios = []
ordem = 1

def criar_polinomio():
    global ordem
    coeficientes = input("Digite os coeficientes do polinómio separados por espaço: ").split()
    coeficientes = [float(coef) for coef in coeficientes]
    polinomio = coeficientes
    polinomios.append((ordem, polinomio))
    ordem += 1

def ler_polinomios():
    arquivo = input("Digite o nome do arquivo de polinómios: ")
    with open(arquivo, 'r') as file:
        for line in file:
            coeficientes = [float(coef) for coef in line.strip().split()]
            polinomios.append((ordem, coeficientes))
            ordem += 1

def mostrar_polinomios():
    print("Número de ordem\tpolinómio")
    for ordem, polinomio in polinomios:
        print(f"{ordem}\t{polinomio}")

def calcular_polinomio():
    num_ordem = int(input("Digite o número de ordem do polinómio a ser calculado: "))
    x = float(input("Digite o valor de x: "))
    if num_ordem <= len(polinomios):
        ordem, coeficientes = polinomios[num_ordem - 1]
        resultado = sum(c * (x ** i) for i, c in enumerate(coeficientes))
        print(f"Resultado: {resultado}")
    else:
        print("Número de ordem inválido.")

def mostrar_polinomios_com_grau():
    print("Número de ordem\tpolinómio\tGrau")
    for ordem, coeficientes in polinomios:
        grau = len(coeficientes) - 1
        print(f"{ordem}\t{coeficientes}\t{grau}")

def polinomio_maior_grau():
    if polinomios:
        ordem, coeficientes = max(polinomios, key=lambda x: len(x[1]) - 1)
        grau = len(coeficientes) - 1
        print(f"Polinómio de maior grau (Número de Ordem {ordem}): {coeficientes}, Grau: {grau}")
    else:
        print("Nenhum polinómio carregado.")

def somar_polinomios():
    num_ordem1 = int(input("Digite o número de ordem do primeiro polinómio: "))
    num_ordem2 = int(input("Digite o número de ordem do segundo polinómio: "))
    if 1 <= num_ordem1 <= len(polinomios) and 1 <= num_ordem2 <= len(polinomios):
        _, coeficientes1 = polinomios[num_ordem1 - 1]
        _, coeficientes2 = polinomios[num_ordem2 - 1]
        coeficientes_soma = [c1 + c2 for c1, c2 in zip(coeficientes1, coeficientes2)]
        polinomios.append((ordem, coeficientes_soma))
        ordem += 1
        print(f"Resultado da soma (Número de Ordem {ordem}): {coeficientes_soma}")
    else:
        print("Número de ordem inválido.")

def gerar_grafico():
    num_ordem = int(input("Digite o número de ordem do polinómio para gerar o gráfico: "))
    if 1 <= num_ordem <= len(polinomios):
        _, coeficientes = polinomios[num_ordem - 1]
        x = [i for i in range(-10, 11)]
        y = [sum(c * (xi ** i) for i, c in enumerate(coeficientes)) for xi in x]
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(f"Gráfico do polinómio (Número de Ordem {num_ordem})")
        plt.grid()
        plt.show()
    else:
        print("Número de ordem inválido.")

def gravar_polinomios():
    arquivo = input("Digite o nome do arquivo de saída: ")
    with open(arquivo, 'w') as file:
        for _, coeficientes in polinomios:
            coef_str = " ".join(map(str, coeficientes))
            file.write(coef_str + "\n")

while True:
    print("\nEscolha uma opção:")
    print("1 -> Criar polinómio")
    print("2 -> Ler polinómios de um arquivo")
    print("3 -> Mostrar polinómios em memória")
    print("4 -> Calcular valor de um polinómio")
    print("5 -> Mostrar polinomios com grau")
    print("6 -> Mostrar polinómio de maior grau")
    print("8 -> Somar dois polinómios")
    print("9 -> Gerar gráfico de um polinómio")
    print("10 -> Gravar polinómios em um arquivo")
    print("0 -> Sair")

    opcao = input("Opção: ")

    if opcao == '1':
        criar_polinomio()
    elif opcao == '2':
        ler_polinomios()
    elif opcao == '3':
        mostrar_polinomios()
    elif opcao == '4':
        calcular_polinomio()
    elif opcao == '5':
        mostrar_polinomios_com_grau()
    elif opcao == '6':
        polinomio_maior_grau()
    elif opcao == '8':
        somar_polinomios()
    elif opcao == '9':
        gerar_grafico()
    elif opcao == '10':
        gravar_polinomios()
    elif opcao == '0':
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

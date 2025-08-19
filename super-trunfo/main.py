from super_trunfo.game import carregar_baralho, sortear_duas_cartas, comparar, atributos_disponiveis

def mostrar_carta(carta):
    print(f"\n=== {carta.nome} ===")
    for k, v in carta.atributos.items():
        print(f"- {k}: {v}")

def escolher_atributo(lista):
    print("\nEscolha um atributo para disputar:")
    for i, a in enumerate(lista, start=1):
        print(f"{i}. {a}")
    while True:
        try:
            escolha = int(input("Digite o número do atributo: "))
            if 1 <= escolha <= len(lista):
                return lista[escolha - 1]
        except ValueError:
            pass
        print("Entrada inválida. Tente novamente.")

def jogar():
    baralho = carregar_baralho()
    atts = atributos_disponiveis(baralho)

    print("Bem-vinda(o) ao Super Trunfo (versão simples)!")
    pontos_voce = 0
    pontos_pc = 0

    while True:
        sua_carta, carta_pc = sortear_duas_cartas(baralho)

        print("\n-----------------------------------------")
        print(f"Placar: Você {pontos_voce} x {pontos_pc} Computador")
        mostrar_carta(sua_carta)

        atributo = escolher_atributo(atts)
        print(f"\nVocê escolheu: {atributo}")

        # Revela carta do PC
        print("\nCarta do computador:")
        mostrar_carta(carta_pc)

        resultado = comparar(sua_carta, carta_pc, atributo)
        if resultado == 1:
            print("\n>> Você venceu a rodada!")
            pontos_voce += 1
        elif resultado == -1:
            print("\n>> O computador venceu a rodada.")
            pontos_pc += 1
        else:
            print("\n>> Empate!")

        cont = input("\nJogar outra rodada? (s/n): ").strip().lower()
        if cont != 's':
            break

    print(f"\nFim de jogo! Placar final: Você {pontos_voce} x {pontos_pc} Computador")
    print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar()

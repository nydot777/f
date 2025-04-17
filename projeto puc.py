# Lista para armazenar os nomes dos estudantes
estudantes = []

while True:
    # Mostrando o menu principal
    print("\nMenu Principal")
    print("1- Estudantes")
    print("2- Professores")
    print("3- Disciplinas")
    print("4- Matrículas")
    print("5- Turmas")
    print("0- Sair")

    # Opção do menu principal
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\nVocê escolheu Estudantes.")
        
        while True:
            print("\nMenu de Operações - Estudantes")
            print("1- Incluir")
            print("2- Listar")
            print("3- Atualizar")
            print("4- Excluir")
            print("5- Voltar")

            segundo_menu = int(input("Escolha uma opção: "))

            if segundo_menu == 1:
                nome = input("Digite o nome do estudante: ").strip()
                if nome:
                    estudantes.append(nome)
                    print(f"Estudante '{nome}' cadastrado com sucesso!")
                else:
                    print("Nome inválido. Tente novamente.")

            elif segundo_menu == 2:
                if estudantes:
                    print("\nLista de Estudantes:")
                    for i, estudante in enumerate(estudantes, start=1):
                        print(f"{i}. {estudante}")
                else:
                    print("Não há estudantes cadastrados.")

            elif segundo_menu in [3, 4]:
                print("EM DESENVOLVIMENTO")

            elif segundo_menu == 5:
                print("Voltando para o menu principal...")
                break

            else:
                print("Você escolheu uma opção inválida.")

    elif opcao in [2, 3, 4, 5]:
        print("EM DESENVOLVIMENTO")

    elif opcao == 0:
        print("Saindo do menu...")
        break

    else:
        print("Você escolheu uma opção inválida.")

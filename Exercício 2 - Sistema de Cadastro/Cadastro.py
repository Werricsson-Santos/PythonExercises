# --------------- Início das Variáveis Globais --------------- #
lista_pecas = []
codigo = 0


# --------------- Fim das Variáveis Globais ---------------#

# --------------- Início da Função cadastrarPeca() --------------- #

def cadastrarPeca(codigo):
    print(
        '\033[1;97m' + '\nVocê selecionou a opção\033[0m \033[1;4;34mCadastrar Peça:\033[0m\n' + f"Código da peça: {codigo}")
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o nome do fabricante: ')
    fabricante = fabricante.lower().strip()
    while True:  # Laço infinito para forçar que o usuário digite um valor numérico.
        try:
            value = float(input('Digite o valor(R$) da peça: '))
            valor = f"R$ {value:.2f}"  # Formata o valor digitado pelo o usuário para o formato (R$ 00.00).
            break
        except ValueError:  # Caso o usuário digite um valor que não seja númerico o programa retorna ao input - value.
            print('\033[1;4;91m' + '\nO valor deve ser um número decimal\n' + '\033[0m')
            continue  # Retorna ao início do laço (input - value).

    # Cria um dicionário(peça) contendo cada valor digitado pelo usuário:
    peca = {'Codigo': codigo,
            'Nome': nome,
            'Fabricante': fabricante,
            'Valor': valor}
    lista_pecas.append(peca)  # Insere o dicionário(peça) criado pelo usuário na lista_pecas.

    # Retorna um print ao usuario para que ele possa visualizar a peça que cadastrou:
    print('\033[1;3;4;34m' + '\nPeça cadastrada com sucesso!\n' + '\033[0m' +
          f"\033[97mCodigo:\033[0m \033[34m{peca['Codigo']}\033[0m\n"
          f"\033[97mNome:\033[0m \033[34m{peca['Nome']}\033[0m\n"
          f"\033[97mFabricante:\033[0m \033[34m{peca['Fabricante']}\033[0m\n"
          f"\033[97mValor:\033[0m \033[34m{peca['Valor']}\033[0m")


# --------------- Fim da Função cadastrarPeca() --------------- #

# --------------- Início da Função consultarPeca() --------------- #
def consultarPeca():
    while True:  # Laço infinito para forçar que o usuário digite uma opção contida no menu (input - opcao_consulta).
        opcao_consulta = input('\n1 - Consultar TODAS as peças \n' +
                               '2 - Consultar peças por CODIGO \n' +
                               '3 - Consultar peças por FABRICANTE \n' +
                               '4 - Retornar \n' + '>> ')
        # Estrutura condicional para chamar as funções correspondentes a escolha da opção contida no menu (input - opcao_consulta).
        if opcao_consulta == '1':
            print('\033[1;97m' + '\nVocê selecionou a opção\033[0m \033[1;4;34mConsultar TODAS as peças:\n' + '\033[0m')
            encontrou = False  # Enquanto essa tag for false o programa não passa pelo laço "for" logo abaixo.

            # Fazendo uma iteração em cada dicionário da lista_pecas:
            for peca in lista_pecas:
                encontrou = True
                print(
                    '\033[1;93m' + '\n-----------------------------------\n' + '\033[0m')  # Separação entre os dicionários.
                # Fazendo uma iteração em cada item (par - chave:dado) contido em cada dicionário da lista_pecas:
                for key, value in peca.items():
                    print(
                        f"\033[1;97m{key}:\033[0m \033[34m{value}\033[0m")  # Retorna o print de cada item do dicionário (par - chave:dado).
                print(
                    '\033[1;93m' + '\n-----------------------------------\n' + '\033[0m')  # Separação entre os dicionários.

            if not encontrou:  # Caso não haja nenhuma peça cadastrada na lista_pecas.
                print('\033[1;4;91m' + '\nNão existe nenhuma peça cadastrada...\n' + '\033[0m')

        elif opcao_consulta == '2':
            print('\033[1;97m' + '\nVocê selecionou a opção\033[0m \033[1;4;34mConsultar peças por CODIGO:' + '\033[0m')
            while True:
                try:
                    codigo_consulta = int(input('Digite o CODIGO do produto que deseja consultar: '))
                    # Fazendo uma iteração em cada dicionário da lista_pecas:
                    for peca in lista_pecas:
                        # Estrutura condicional que verifica se existe algum dicionário(peça) onde a chave "Codigo" tenha o mesmo valor digitado pelo usuário:
                        if peca['Codigo'] == codigo_consulta:
                            print(
                                '\033[1;93m' + '\n-----------------------------------\n' + '\033[0m')  # Separação entre os dicionários.
                            for key, value in peca.items():  # Fazendo uma iteração em cada item (par - chave:dado) contido em cada dicionário da lista_pecas:
                                print(
                                    f"\033[1;97m{key}:\033[0m \033[34m{value}\033[0m")  # Retorna um print do dicionário(peça) encontrado ao usuário. E retorna ao menu (input - opcao_consulta)
                            print(
                                '\033[1;93m' + '\n-----------------------------------\n' + '\033[0m')  # Separação entre os dicionários.
                            return consultarPeca()  # Retorna ao início dessa função, para manter o padrão dos demais tipos de consultas.

                    else:  # Caso não exista nenhum dicionário(peça) com a chave "Codigo" contendo o valor igual ao valor digitado pelo usuário. O programa retorna ao menu (input - opcao_consulta).
                        print('\033[1;4;91m' + '\nNão existe nenhuma peça registrada com esse código.\n' + '\033[0m')
                        return consultarPeca()  # Retorna ao início dessa função, para manter o padrão dos demais tipos de consultas.

                except ValueError:  # Caso o usuário digite um valor que não seja númerico o programa retorna ao input - opcao_consulta.
                    print(
                        '\033[1;4;91m' + '\nVocê deve digitar um número (Os códigos das peças cadastradas possuem um valor numérico).\n' + '\033[0m')
                    continue  # Retorna ao início do laço (input - opcao_consulta).



        elif opcao_consulta == '3':
            print(
                '\033[1;97m' + '\nVocê selecionou a opção\033[0m \033[1;4;34mConsultar peças por FABRICANTE:' + '\033[0m')
            consulta_fabricante = input('Digite o nome do FABRICANTE: ')
            consulta_fabricante = consulta_fabricante.lower().strip()

            encontrou = False  # Enquanto essa tag for false o programa não passa pelo laço "for" logo abaixo. Trabalhando com o else, eu teria que utilizar um break ou return após o if e dessa forma o programa retornaria apenas o primeiro dicionário encontrado.

            # Fazendo uma iteração em cada dicionário da lista_pecas:
            for peca in lista_pecas:
                # Estrutura condicional que verifica se existe algum dicionário(peça) onde a chave "Fabricante" tenha o mesmo valor digitado pelo usuário.
                if peca['Fabricante'] == consulta_fabricante:
                    encontrou = True  # Quando o fabricante que o usuário digitou existir na lista_pecas, o programa executa o laço abaixo para trazer todos os items desse dicionário. Quando não houver mais match ele não executará o laço abaixo novamente.
                    print(
                        '\033[1;93m' + '\n-----------------------------------\n' + '\033[0m')  # Separação entre os dicionários.
                    # Fazendo uma iteração em cada item (par - chave:dado) contido em cada dicionário da lista_pecas:
                    for key, value in peca.items():
                        print(
                            f"\033[1;97m{key}:\033[0m \033[34m{value}\033[0m")  # Retorna um print do dicionário(peça) encontrado ao usuário. E retorna ao menu (input - opcao_consulta)
                    print(
                        '\033[1;93m' + '\n-----------------------------------\n' + '\033[0m')  # Separação entre os dicionários.

            if not encontrou:  # Caso não exista nenhum dicionário(peça) com a chave "Fabricante" contendo o valor igual ao valor digitado pelo usuário. O programa retorna ao menu (input - opcao_consulta).
                print('\033[1;4;91m' + '\nNão existe nenhum Fabricante registrado com esse nome.\n' + '\033[0m')


        elif opcao_consulta == '4':  # Caso o usuário escolha sair do menu de consultas.
            print('\033[1;3;4;34m' + 'Retornando ao menu principal...' + '\033[0m')
            break  # Encerra o laço consequentemente encerrando a função e retorna ao programa principal.

        else:  # Caso o usuário digite uma opção inválida o programa deve retornar ao início do laço (input - opcao_consulta).
            print('\033[1;4;97;101m' + '\n Opção inválida! \n' + '\033[0m')
            continue  # Retona ao início do laço (input - opcao_consulta).


# --------------- Fim da Função consultarPeca() --------------- #

# --------------- Início da Função removerPeca() --------------- #
def removerPeca():
    print('\033[1;97m' + '\nVocê selecionou a opção\033[0m \033[1;4;34mRemover Peças:' + '\033[0m')

    while True:
        try:
            remover = int(input('Digite o CODIGO da peça que deseja REMOVER: '))
            # Fazendo uma iteração em cada dicionário da lista_pecas:
            for peca in lista_pecas:
                # Estrutura condicional que verifica se existe algum dicionário(peça) onde a chave "Codigo" tenha o mesmo valor digitado pelo usuário.
                if peca['Codigo'] == remover:
                    # Retorna um print ao usuário para que ele possa visualizar a peça que ele irá remover.
                    print(f"\033[1;97;101m\nA seguinte peça será removida:\033[0m\n"
                          f"\033[97mCodigo:\033[0m        \033[1;34m{peca['Codigo']}\033[0m\n"
                          f"\033[97mNome:\033[0m          \033[1;34m{peca['Nome']}\033[0m\n"
                          f"\033[97mFabricante:\033[0m    \033[1;34m{peca['Fabricante']}\033[0m\n"
                          f"\033[97mValor:\033[0m         \033[1;34m{peca['Valor']}\033[0m")
                    while True:  # Laço infinito para forçar o usuário a responder se ele realmente deseja remover a peça selecionada.
                        confirma = input('\nTem certeza que dejesa remover a peça acima (S/N)? ')
                        confirma = confirma.upper().replace(' ', '')

                        if confirma == 'S':
                            print(f"\033[1;34m\nPeça removida com sucesso!\033[0m")
                            lista_pecas.remove(peca)  # Remove o dicionário(peça) selecionado pelo usuário.
                            return  # Retorna ao menu principal.

                        elif confirma == 'N':
                            print(f"\033[1;97m\nOperação cancelada!\033[0m"
                                  f"\033[1;34m\nRetornando ao menu principal...\033[0m")
                            return  # Retorna ao menu principal.

                        else:  # Caso o usuário digite uma opção inválida o programa deve retornar ao início do laço (input - confirma).
                            print('\033[1;4;97;101m' + '\n Opção inválida! \n' + '\033[0m')
                            continue  # Retona ao início do laço (input - confirma).


            else:  # Caso não exista nenhum dicionário(peça) com a chave "Codigo" contendo o valor igual ao valor digitado pelo usuário. O programa retorna ao menu principal.
                print(
                    '\033[1;4;91m' + '\nNão existe nenhuma peça registrada com esse código para que possa ser removida.\n' + '\033[0m')
                return  # Retorna ao menu principal.

        except ValueError:  # Caso o usuário digite um valor que não seja númerico o programa retorna ao input - remover.
            print(
                '\033[1;4;91m' + '\nVocê deve digitar um número (Os códigos das peças cadastradas possuem um valor numérico).\n' + '\033[0m')
            continue  # Retorna ao início do laço (input - remover).


# --------------- Fim da Função removerPeca() --------------- #


# --------------- Início do Programa --------------- #

# Identificador pessoal:
print('\033[1;97m' + 'Bem Vindo ao Controle de Estoque da Bicicletaria do \033[4;34mWerricsson Santos.\033[0m')

while True:  # Laço infinito para forçar que o usuário digite uma opção contida no menu (input - opcao_principal).
    opcao_principal = input('\nEscolha a opção desejada:\n' +
                            '1 - Cadastrar Peças\n' +
                            '2 - Consultar Peças\n' +
                            '3 - Remover Peças\n' +
                            '4 - Sair\n' + '>> ')
    # Estrutura condicional para chamar as funções correspondentes a escolha da opção contida no menu (input - opcao_principal).
    if opcao_principal == '1':
        codigo += 1
        cadastrarPeca(codigo)

    elif opcao_principal == '2':
        consultarPeca()

    elif opcao_principal == '3':
        removerPeca()

    elif opcao_principal == '4':  # Caso o usuário deseje encerrar o programa.
        print('\033[3;4;34m' + 'Encerrando o programa...')
        break  # Encerra o laço consequentemente encerrando o programa.

    else:  # Caso o usuário digite uma opção inválida o programa retorna ao início do laço (input - opcao_principal).
        print('\033[1;4;97;101m' + '\n Opção inválida! \n' + '\033[0m')
        continue  # retorna ao início do laço (input - opcao_principal).

# --------------- Fim do Programa --------------- #
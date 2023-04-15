# Crianco funções para facilitar o print da tabela:
# Table Header (Cabeçalho da Tabela) - Essa função cria um realce para o ínicio de uma tabela onde contém os cabeçalhos.
def th3(s1, s2, s3=''):  # Apenas 3 cabeçalhos/colunas.
    tam = len(s1 + s2 + s3) + 6

    if tam:
        print('\033[1;93m' + '+', '-' * tam, '+' + '\033[0;0m')
        print('\033[1;93m|\033[0;0m', '\033[1;34m' + s1 + '\033[0m', '\033[1;93m|\033[0;0m',
              '\033[1;34m' + s2 + '\033[0m', '\033[1;93m|\033[0;0m',
              '\033[1;34m' + s3 + '\033[0m', '\033[1;93m|\033[0;0m')
        print('\033[1;93m' + '|' + '-' * tam + '--|' + '\033[0;0m')


# Table Rows (Linhas da Tabela) - Essa função cria um realce para as linhas de uma tabela onde contém os itens.
def tr3(s1, s2, s3=''):  # Apenas 3 itens/colunas.
    tam1 = len(s1)
    tam2 = len(s2)
    tam3 = len(s3)
    tamTotal = len(s1 + s2 + s3)
    if tamTotal:
        print('\033[1;93m|\033[0;0m', s1, '\033[1;93m|\033[0;0m', s2, '\033[1;93m|\033[0;0m', s3,
              '\033[1;93m|\033[0;0m')
        print('\033[1;93m' + '|' + ' ' * tam1 + '  |' + ' ' * tam2 + '  |' + ' ' * tam3 + '  |' + '\033[0;0m')


# Table Footer (Rodapé da Tabela) - Essa função cria um realce para o rodapé de uma tabela (usar para fechar a tabela, colocar os últimos itens).
def tf3(s1, s2, s3=''):  # Apenas 3 itens/colunas.
    tam = len(s1 + s2 + s3) + 6
    if tam:
        print('\033[1;93m|\033[0;0m', s1, '\033[1;93m|\033[0;0m', s2, '\033[1;93m|\033[0;0m', s3,
              '\033[1;93m|\033[0;0m')
        print('\033[1;93m' + '+', '-' * tam, '+' + '\033[0;0m')


# Identificador pessoal:
print('\033[1;97m' + 'Bem Vindo a Lanchonete do \033[4;34mWerricsson Santos\033[0m\033[1;97m! \n')

# Inicio do Programa:
print('\033[1;93m                  Cardápio')
th3('Código', '      Descrição      ', 'Valor(R$)')
tr3(' 100  ', '   Cachorro-Quente   ', '   9,00  ')
tr3(' 101  ', 'Cachorro-Quente Duplo', '  11,00  ')
tr3(' 102  ', '       X-Egg         ', '  12,00  ')
tr3(' 103  ', '      X-Salada       ', '  13,00  ')
tr3(' 104  ', '      X-Bacon        ', '  14,00  ')
tr3(' 105  ', '       X-Tudo        ', '  17,00  ')
tr3(' 200  ', '  Refrigerante Lata  ', '   5,00  ')
tf3(' 201  ', '      Chá Gelado     ', '   4,00  ')
print(
    '\033[1;97m' + ' Digite \033[0m\033[1;4;97;101m SAIR \033[0m \033[1;97mcaso queira desistir da compra.' + '\033[0m \n')

acumulador = 0.00  # Iniciando o acumulador zerado para poder somar os valores do pedido.
encerrar = False
# Laço de repetição infinito para forçar a escolha de um produto contido na tabela:
while not encerrar:
    # Início
    codigo = input('\nInsira o código desejado (Consultar tabela): \n' + '>>')
    # Tratando os dados inseridos pelo cliente, para o caso dele digitar "sair".

    # Método upper(transforma todas as strings em maiúsculas.). Método replace('valor que deseja alterar', 'valor desejado'). Faz a substituição de uma string.
    codigo = codigo.upper().replace(' ', '')  # Encadeamento de métodos de uma função. Para economizar uma linha.
    """
    Poderíamos usar o método strip(), porém ele remove apenas os espaços contidos antes e depois do ínicio de uma string. O replace nos permite retirar todos os espaços.
    Isso é útil para o pior cenário, caso o cliente digite ' s  a  i  r  '.
    """

    # Estrutura condicional para capturar a escolha do cliente. Força a escolha de uma opção válida e faz uma iteração no acumulador para somar os valores dos produtos escolhidos.
    if codigo == '100':
        print(
            '\033[3;97m' + 'você escolheu um \033[0m\033[1;4;34mCachorro-Quente\033[0m\033[3;97m no valor de \033[0m\033[1;4;34mR$9,00 \n' + '\033[0m')
        acumulador += 9

    elif codigo == '101':
        print(
            '\033[3;97m' + 'você escolheu um \033[0m\033[1;4;34mCachorro-Quente Duplo\033[0m\033[3;97m no valor de \033[0m\033[1;4;34mR$11,00 \n' + '\033[0m')
        acumulador += 11

    elif codigo == '102':
        print(
            '\033[3;97m' + 'você escolheu um \033[0m\033[1;4;34mX-Egg\033[0m\033[3;97m no valor de \033[0m\033[1;4;34mR$12,00' + '\033[0m \n')
        acumulador += 12

    elif codigo == '103':
        print(
            '\033[3;97m' + 'você escolheu um \033[0m\033[1;4;34mX-Salada\033[0m\033[3;97m no valor de \033[0m\033[1;4;34mR$13,00' + '\033[0m \n')
        acumulador += 13

    elif codigo == '104':
        print(
            '\033[3;97m' + 'você escolheu um \033[0m\033[1;4;34mX-Bacon\033[0m\033[3;97m no valor de \033[0m\033[1;4;34mR$14,00' + '\033[0m \n')
        acumulador += 14

    elif codigo == '105':
        print(
            '\033[3;97m' + 'você escolheu um \033[0m\033[1;4;34mX-Tudo\033[0m\033[3;97m no valor de \033[0m\033[1;4;34mR$17,00' + '\033[0m \n')
        acumulador += 17

    elif codigo == '200':
        print(
            '\033[3;97m' + 'você escolheu um \033[0m\033[1;4;34mRefrigerante Lata\033[0m\033[3;97m no valor de \033[0m\033[1;4;34mR$5,00' + '\033[0m \n')
        acumulador += 5

    elif codigo == '201':
        print(
            '\033[3;97m' + 'você escolheu um \033[0m\033[1;4;34mChá Gelado\033[0m\033[3;97m no valor de \033[0m\033[1;4;34mR$4,00' + '\033[0m \n')
        acumulador += 4
    # Caso alguma das condicionais acima seja verdadeira(true), é feito uma iteração/soma no acumulador e o programa segue para o próximo laço contendo o input(pedir_mais).

    elif codigo == 'SAIR':  # Essa opção está fora do cardápio, para caso o cliente desista da compra ou caso ele diga sim na opção de pedir mais, mas acaba desistindo depois.
        if acumulador == 0:  # Neste caso o cliente não escolheu nada, portanto não há valores a serem cobrados.
            print('\033[3;34m' + 'Encerrando o programa...')
            break  # Encerra o programa.

        else:  # Neste caso o cliente já havia escolhido algum produto, só decidiu não pedir mais nada. Portanto há valores a serem cobrados.
            print('\033[3;97m' + 'O total a ser pago é: \033[0m\033[1;4;34mR${:.2f}'.format(acumulador))
            break  # Encerra o programa.

    else:  # Caso o cliente digite qualquer coisa diferente de um dos códigos contidos no cardápio, o programa força ele a digitar uma opção válida.
        print('\033[1;4;97;101m' + ' Opção inválida! ' + '\033[0m \n')
        continue  # Volta ao início do laço principal.

    # Aninhando outro laço infinito dentro do laço principal para forçar o cliente a responder (S | N) no input pedir_mais. Não faz sentido ele digitar algo errado e retornar pro laço principal.
    while True:
        pedir_mais = input('Você deseja pedir mais alguma coisa (S/N)?\n' + '>>')
        pedir_mais = pedir_mais.upper().strip()

        if pedir_mais == 'S':
            break  # Encerra esse laço e retorna ao início do laço principal (input codigo).

        elif pedir_mais == 'N':  # Caso o cliente não queira pedir mais nada, os dois laços devem ser encerrados.
            print('\033[3;97m' + 'O total a ser pago é: \033[0m\033[1;4;34mR${:.2f}'.format(
                acumulador))  # Retorna o valor que o cliente deve pagar
            encerrar = True  # Atribui o valor "True" para a variável "encerrar", isso impede do programa executar o primeiro laço infinito.
            break  # Encerra esse laço e retorna ao laço principal, porém como a variável "encerrar" está recebendo o valor "True" o primeiro laço não será executado!

        else:  # Caso o cliente digite uma opção inválida, ele deve permanecer preso nesse laço secundário.
            print('\033[1;4;97;101m' + ' Opção inválida! \n' + '\033[0m')
            continue  # Retorna ao início do laço secundário (input pedir_mais).
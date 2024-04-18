AGENDA = {}


def mostrar_contatos():

    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)

    else:
        print('A agenda de contato está vazia')


def buscar_contato(contato):

    contato = contato.lower()

    try:
        for key in AGENDA.keys():

            if key.lower() == contato:
                print('Nome: ', key)
                print('Telefone', AGENDA[key]['Telefone'])
                print('E-mail', AGENDA[key]['E-mail'])
                print('Endereço', AGENDA[key]['Endereço'])
                print('------------------------------------------------------------')
                return
        print('Conctato inexistente')
    except Exception as error:
        print('Ocorrou um erro')


def criar_contato(telefone, email, endereco):

    return {
        'Telefone': telefone,
        'E-mail': email,
        'Endereço': endereco,
    }


def solicitar_detalhes_contato():
    contato = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o e-mail do contato: ')
    endereco = input('Digite o endereço do contato: ')

    return contato, telefone, email, endereco

def incluir_contato(contato, telefone, email, endereco):

    if contato in AGENDA:
        print('Contato {} já existe'.format(contato))
    else:
        AGENDA[contato] = criar_contato(telefone, email, endereco)
        print('Contato {} inserido com sucesso!'.format(contato))
    print('------------------------------------------------------------')


def editar_contato(contato, telefone, email, endereco):

    if contato in AGENDA:
        AGENDA[contato] = criar_contato(telefone, email, endereco)
        print('Contato {} editado com sucesso!'.format(contato))
    else:
        print('Contato {} não encontrado na agenda'.format(contato))
        print('------------------------------------------------------------')


def excluir_contato(contato):

    contato = contato.lower()

    if contato in AGENDA:
        del AGENDA[contato]
        print('Contato {} excluído com sucesso!'.format(contato))
        print('------------------------------------------------------------')
    else:
        print('Contato inexistente')


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                contato, telefone, email, endereco = linha.strip().split(';')
                incluir_contato(contato, telefone, email, endereco)
        print('Contatos importado com sucesso!')

        exportar_contatos()

    except FileExistsError:
        print('Arquivo não encontrado')
    except Exception as error:
        print('Algum erro aconteceu')


def exportar_contatos():
    try:
        with open('agenda.csv', 'w') as arquivo:
            arquivo.write('Nome: --- Telefone: --- E-mail: --- Endereço: \n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['Telefone']
                email = AGENDA[contato]['E-mail']
                endereco = AGENDA[contato]['Endereço']
                arquivo.write('{}; {}; {}; {}\n'.format(contato, telefone, email, endereco))
        print('Agenda exportada com sucesso!')
    except:
        print('Erro ao exportar o agenda')


def salvar_contatos():
    exportar_contatos('agenda.csv')


def carregar_contatos():
    try:
        with open('agenda.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                solicitar_detalhes_contato =  linha.strip().split(';')

                nome = solicitar_detalhes_contato[0]
                telefone = solicitar_detalhes_contato[1]
                email = solicitar_detalhes_contato[2]
                endereco = solicitar_detalhes_contato[3]

                AGENDA[nome] = {
                    'Telefone': telefone,
                    'E-mail': email,
                    'Endereço': endereco,
                }
            print('>>>> Database carregado com sucesso')
            print('>>>> {} contatos carregados'.format(len(AGENDA)))

    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)


def imprimir_menu():
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Importar contato de um arquivo CSV')
    print('7 - Exportar contato para CSV')
    print('0 - Fechar agenda')
    print('------------------------------------------------------------')


exportar_contatos()

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')

        buscar_contato(contato)

    elif opcao == '3':
        contato, telefone, email, endereco = solicitar_detalhes_contato()

        incluir_contato(contato, telefone, email, endereco)

    elif opcao == '4':
        contato, telefone, email, endereco = solicitar_detalhes_contato()

        editar_contato(contato, telefone, email, endereco)

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')

        excluir_contato(contato)

    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo que você deseja importar: ')
        importar_contatos(nome_do_arquivo)

    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo que você deseja exportar: ')
        exportar_contatos()

    elif opcao == '0':
        print('Fechando o programa')
        break

    else:
        print('Opção inválida')
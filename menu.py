from onibus import Onibus
from funcionario import Funcionario
from sistema import Sistema
from parada import Parada

sistema = Sistema()

# Números dos menus
MENU_PRINCIPAL = 0
MENU_CRIACAO = 1
MENU_LISTAR = 2
MENU_ATRIBUICAO = 3
MENU_ALTERACAO = 4
MENU_EXCLUSAO = 5

textos_menu = [
       ['Sair do Programa',
        'Criação (Fiscal, Motorista, Ônibus, Parada)',
        'Listar todos (Fiscal, Motorista, Ônibus, Paradas, Rotas)',
        'Atribuição (Fiscal/Motorista/Parada ao ônibus)',
        'Alteração de dados (Fiscal, Motorista, Ônibus, Parada)',
        'Exclusão de dados (Fiscal, Motorista, Ônibus, Parada)'],
        ['Voltar ao Menu Principal',
        'Criar Fiscal',
        'Criar Motorista',
        'Criar Ônibus',
        'Criar Parada'],
        ['Voltar ao Menu Principal',
        'Listar Fiscais',
        'Listar Motoristas',
        'Listar Ônibus',
        'Listar Paradas',
        'Listar Rotas'],
        ['Voltar ao Menu Principal',
        'Atribuir Fiscal a Ônibus',
        'Atribuir Motorista a Ônibus',
        'Adicionar Parada a Ônibus'],
        ['Voltar ao Menu Principal',
        'Alterar Nome do Fiscal',
        'Alterar Idade do Fiscal',
        'Alterar Nome do Motorista',
        'Alterar Idade do Motorista',
        'Alterar Código do Ônibus',
        'Alterar Rota do Ônibus',
        'Alterar Preço da Passagem do Ônibus',
        'Alterar Código da Parada',
        'Alterar Endereço da Parada'],
        ['Voltar ao Menu Principal',
        'Excluir Fiscal',
        'Excluir Motorista',
        'Excluir Ônibus',
        'Excluir Parada'],
        ]

sistema.criar_motorista(Funcionario('Motorista 1' , 48))
sistema.criar_motorista(Funcionario('Motorista 2', 55))
sistema.criar_motorista(Funcionario('Motorista 3', 25))

sistema.criar_fiscal(Funcionario('Fiscal A', 21))
sistema.criar_fiscal(Funcionario('Fiscal B', 30))
sistema.criar_fiscal(Funcionario('Fiscal C', 44))

sistema.criar_onibus(Onibus(551))
sistema.criar_onibus(Onibus(355))
sistema.criar_onibus(Onibus(721))

sistema.criar_parada(Parada(12, "Av. Vicente de Carvalho, 1483"))
sistema.criar_parada(Parada(22, "Av. Meriti, 999"))
sistema.criar_parada(Parada(33, "Rua Pascal, 131"))

def escolher_acao(i_menu, limite):
    print("-"*25 + "MENU" + "-"*25)
    i = 0
    for texto in textos_menu[i_menu]:
        print(i, " - ", texto)
        i += 1
    while(True):
        op = input("Escolha uma opção:")
        if op.isdigit():
            op = int(op)
            if(op >= 0 and op <= limite):
                return op
            else:
                print("Opção inválida!")
        else:
            print("Opção inválida!")

def escolher_objeto(lista):
    i = 0
    for objeto in lista:
        if isinstance(objeto, Funcionario):
            print(i, " - ", objeto.nome)
        elif isinstance(objeto, Onibus):
            print(i, " - ", objeto.codigo)
        elif isinstance(objeto, Parada):
            print(i, " - ", objeto.endereco)
        i += 1
    if isinstance(objeto, Funcionario):
        tipo_objeto = "do Funcionário: "
    elif isinstance(objeto, Onibus):
        tipo_objeto = "do Ônibus: "
    elif isinstance(objeto, Parada):
        tipo_objeto = "da Parada: "
    while(True):
        op = input("Escolha o ID " + tipo_objeto)
        if op.isdigit():
            op = int(op)
            if(op >= 0 and op <= len(lista)-1):
                return op
            else:
                print("Opção inválida!")
        else:
            print("Opção inválida!")

menu_atual = MENU_PRINCIPAL

while(menu_atual!= -1):
    escolha = escolher_acao(menu_atual, len(textos_menu[menu_atual])-1)

    if(menu_atual == MENU_PRINCIPAL):
        if(escolha == 0):
            print("Fim do programa.")
            menu_atual = -1
        else:
            menu_atual = escolha

    elif(menu_atual == MENU_CRIACAO):

        if(escolha == 0):
            menu_atual = MENU_PRINCIPAL
        
        elif(escolha == 1):
            nome = input("Digite o nome do fiscal: ")
            while(True):
                idade = input("Digite a idade do fiscal: ")
                if idade.isdigit():
                    idade = int(idade)
                    break
                else:
                    print("Valor inválido!")
            sistema.criar_fiscal(Funcionario(nome, idade))
            print("Fiscal criado!")
        
        elif(escolha == 2):
            nome = input("Digite o nome do motorista: ")
            while(True):
                idade = input("Digite a idade do motorista: ")
                if idade.isdigit():
                    idade = int(idade)
                    break
                else:
                    print("Valor inválido!")
            sistema.criar_motorista(Funcionario(nome, idade))
            print("Motorista criado!")
        
        elif(escolha == 3):
            motoristas_livres = []
            i = 0
            for motorista in sistema.motoristas:
                if motorista.onibus == None:
                    motoristas_livres.append(i)
                i += 1
            if(len(motoristas_livres) == 0):
                print("Não há motoristas disponíveis! Você deve criar um primeiro.")
            else:
                codigo = input("Digite o código do Ônibus: ")
                i = 0
                for j in motoristas_livres:
                    print(i, " - ", sistema.motoristas[j].nome)
                    i += 1
                while(True):
                    id = input("Escolha o ID do motorista: ")
                    if id.isdigit():
                        id = int(id)
                        if(id > len(motoristas_livres)-1):
                            print("ID inválido!")
                        else:
                            break
                    else:
                        print("ID inválido!")
                i_motorista = motoristas_livres[id]
                sistema.criar_onibus(Onibus(codigo))
                i_onibus = len(sistema.onibus)-1
                sistema.atribuir_motorista_onibus(i_motorista, i_onibus)
        
        elif(escolha == 4):
            codigo = input("Digite o código da parada: ")
            endereco = input("Digite o endereço da parada: ")
            sistema.criar_parada(Parada(codigo, endereco))
            print("Parada criada!")


    elif(menu_atual == MENU_LISTAR):
        if(escolha == 0):
            menu_atual = MENU_PRINCIPAL
        if(escolha == 1):
            sistema.listar_fiscais()
        if(escolha == 2):
            sistema.listar_motoristas()
        if(escolha == 3):
            sistema.listar_onibus()
        if(escolha == 4):
            sistema.listar_paradas()
        if(escolha == 5):
            sistema.listar_rotas()

    elif(menu_atual == MENU_ATRIBUICAO):

        if(escolha == 0):
            menu_atual = MENU_PRINCIPAL

        if(escolha == 1):
            i_fiscal = escolher_objeto(sistema.fiscais)
            i_onibus = escolher_objeto(sistema.onibus)
            sistema.atribuir_fiscal_onibus(i_fiscal, i_onibus)
            print("Atribuição realizada!")

        if(escolha == 2):
            i_motorista = escolher_objeto(sistema.motoristas)
            i_onibus = escolher_objeto(sistema.onibus)
            sistema.atribuir_motorista_onibus(i_motorista, i_onibus)
            print("Atribuição realizada!")

        if(escolha == 3):
            i_fiscal = escolher_objeto(sistema.paradas)
            i_onibus = escolher_objeto(sistema.onibus)
            sistema.adicionar_parada_onibus(i_fiscal, i_onibus)
            print("Atribuição realizada!")


    elif(menu_atual == MENU_ALTERACAO):
        
        if(escolha == 0):
            menu_atual = MENU_PRINCIPAL
        
        if(escolha == 1):
            i_fiscal = escolher_objeto(sistema.fiscais)
            nome = input("Digite o novo nome do fiscal: ")
            sistema.fiscais[i_fiscal].nome = nome[0:25]
        
        if(escolha == 2):
            pass
        if(escolha == 3):
            pass
        if(escolha == 4):
            pass
        if(escolha == 5):
            pass
        if(escolha == 6):
            pass
        if(escolha == 7):
            pass
        if(escolha == 8):
            pass
        if(escolha == 9):
            pass

    elif(menu_atual == MENU_EXCLUSAO):

        if(escolha == 0):
            menu_atual = MENU_PRINCIPAL

        if(escolha == 1):
            if len(sistema.fiscais) > 0:
                i_fiscal = escolher_objeto(sistema.fiscais)
                sistema.deletar_fiscal(i_fiscal)
                print("Fiscal deletado!")
            else:
                print("Erro: Sistema não possui fiscais.")

        if(escolha == 2):
            if len(sistema.motoristas) > 0:
                i_motorista = escolher_objeto(sistema.motoristas)
                sistema.deletar_motorista(i_motorista)
                print("Motorista deletado!")
            else:
                print("Erro: Sistema não possui motoristas.")

        if(escolha == 3):
            if len(sistema.onibus) > 0:
                i_onibus = escolher_objeto(sistema.onibus)
                sistema.deletar_onibus(i_onibus)
                print("Ônibus deletado!")
            else:
                print("Erro: Sistema não possui ônibus.")
        
        if(escolha == 4):
            if len(sistema.paradas) > 0:
                i_parada = escolher_objeto(sistema.paradas)
                sistema.deletar_parada(i_parada)
                print("Parada deletada!")
            else:
                print("Erro: Sistema não possui paradas.")

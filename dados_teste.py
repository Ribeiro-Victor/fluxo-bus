from sistema import Sistema
from funcionario import Funcionario
from onibus import Onibus
from parada import Parada

sistema = Sistema()
def criar_dados_teste():
    sistema.criar_motorista(Funcionario('Antonio' , 48))
    sistema.criar_motorista(Funcionario('Bruno', 55))
    sistema.criar_motorista(Funcionario('Carlos', 25))

    sistema.criar_fiscal(Funcionario('Ana', 21))
    sistema.criar_fiscal(Funcionario('Beatriz', 30))
    sistema.criar_fiscal(Funcionario('Carol', 44))

    sistema.criar_onibus(Onibus('355'))
    sistema.atribuir_motorista_onibus(0, 0)
    sistema.criar_onibus(Onibus('551'))
    sistema.atribuir_motorista_onibus(1, 1)
    sistema.criar_onibus(Onibus('721'))
    sistema.atribuir_motorista_onibus(2, 2)

    sistema.criar_parada(Parada('01', "Av. Vicente de Carvalho, 1483"))
    sistema.criar_parada(Parada('02', "Av. Meriti, 999"))
    sistema.criar_parada(Parada('03', "Rua Pascal, 131"))

    sistema.adicionar_parada_onibus(0, 0)
    sistema.adicionar_parada_onibus(1, 0)
    sistema.adicionar_parada_onibus(2, 0)
    sistema.adicionar_parada_onibus(0, 1)
    sistema.adicionar_parada_onibus(0, 2)
    
    return sistema
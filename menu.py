from onibus import Onibus
from funcionario import Funcionario
from sistema import Sistema
from parada import Parada

sistema = Sistema()


sistema.criar_motorista(Funcionario('Motorista 1' , 48))
sistema.criar_motorista(Funcionario('Motorista 2', 55))
sistema.criar_motorista(Funcionario('Motorista 3', 25))

sistema.criar_fiscal(Funcionario('Fiscal A', 21))
sistema.criar_fiscal(Funcionario('Fiscal B', 30))
sistema.criar_fiscal(Funcionario('Fiscal C', 44))

sistema.criar_onibus(Onibus(551, sistema.motoristas[0]))
sistema.criar_onibus(Onibus(355, sistema.motoristas[1]))
sistema.criar_onibus(Onibus(721, sistema.motoristas[2]))

sistema.criar_parada(Parada(12, "Av. Vicente de Carvalho - 1483"))
sistema.criar_parada(Parada(22, "Av. Meriti - 999"))
sistema.criar_parada(Parada(33, "Rua Pascal - 131"))

sistema.adicionar_parada_onibus(0, 0)
sistema.adicionar_parada_onibus(1, 0)

sistema.mostrar_rotas()

# sistema.mostrar_onibus()
# sistema.mostrar_paradas()

# sistema.deletar_parada(1)

# sistema.mostrar_onibus()
# sistema.mostrar_paradas()

#sistema.mostrar_paradas()
#sistema.mostrar_motoristas()
#sistema.mostrar_fiscais()
#sistema.mostrar_onibus()


# sistema.assignar_fiscal_onibus(0, 0)
# assignar_fiscal_onibus(sistema.fiscais[1], sistema.onibus[1])
# assignar_fiscal_onibus(sistema.fiscais[2], sistema.onibus[2])

# sistema.mostrar_fiscais()
# sistema.mostrar_onibus()

# assignar_fiscal_onibus(sistema.fiscais[2], sistema.onibus[0])

# sistema.mostrar_fiscais()
# sistema.mostrar_onibus()

# sistema.mostrar_fiscais()
# sistema.mostrar_onibus()
# sistema.deletar_fiscal(0)
# sistema.mostrar_onibus()
# sistema.mostrar_fiscais()

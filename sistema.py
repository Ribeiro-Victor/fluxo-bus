class Sistema():
    def __init__(self):
        self.motoristas = []
        self.fiscais = []
        self.onibus = []
        self.paradas = []
    
    def criar_motorista(self, funcionario):
        self.motoristas.append(funcionario)
    
    def criar_fiscal(self, funcionario):
        self.fiscais.append(funcionario)

    def criar_onibus(self, onibus):
        self.onibus.append(onibus)
    
    def criar_parada(self, parada):
        self.paradas.append(parada)

    def mostrar_motoristas(self):
        print("+" + "-"*26 + "+" + "-"*12 + "+" + "-"*22 + "+")
        print("|" + "Nome".center(25) + " | " +"Idade".center(10) + " | " + "Ônibus que dirige".center(20) + " |")
        print("+" +  "-"*26 + "+" + "-"*12 + "+" + "-"*22 + "+")
        for motorista in self.motoristas:
            print("|" + str(motorista))
            print("+" + "-"*26 + "+" + "-"*12 + "+" + "-"*22 + "+")

    def mostrar_fiscais(self):
        print("+" + "-"*26 + "+" + "-"*12 + "+" + "-"*22 + "+")
        print("|" + "Nome".center(25) + " | " +"Idade".center(10) + " | " + "Ônibus que fiscaliza".center(20) + " |")
        print("+" + "-"*26 + "+" + "-"*12 + "+" + "-"*22 + "+")
        for fiscal in self.fiscais:
            print("|" + str(fiscal))
            print("+" + "-"*26 + "+" + "-"*12 + "+" + "-"*22 + "+")
    
    def mostrar_onibus(self):
        print("+" + "-"*11 + "+" + "-"*27 + "+" + "-"*27 + "+" + "-"*22 + "+" + "-"*12 + "+")
        print("|" + "Código".center(10) + " | " +"Motorista".center(25) + " | " + "Fiscal".center(25) + " | "
        + "Paradas".center(20) + " | " + "Passagem".center(10) + " |")
        print("+" + "-"*11 + "+" + "-"*27 + "+" + "-"*27 + "+" + "-"*22 + "+" + "-"*12 + "+")
        for onibus in self.onibus:
            print("|" + str(onibus))
            print("+" + "-"*11 + "+" + "-"*27 + "+" + "-"*27 + "+" + "-"*22 + "+" + "-"*12 + "+")
    
    def mostrar_paradas(self):
        print("+" + "-"*11 + "+" + "-"*52 + "+")
        print("|" + "Código".center(10) + " | " +"Endereço".center(50) + " |")
        print("+" + "-"*11 + "+" + "-"*52 + "+")
        for parada in self.paradas:
            print("|" + str(parada))
            print("+" + "-"*11 + "+" + "-"*52 + "+")

    def mostrar_rotas(self):
        for onibus in self.onibus:
            print("Rota do Ônibus: " + str(onibus.codigo))
            for p in onibus.paradas:
                for parada in self.paradas:
                    if parada.codigo == p:
                        print(parada.endereco)
            print("")
        
    
    def deletar_onibus(self, indice):
        removido = self.onibus.pop(indice)
        if(removido.motorista != None):
            removido.motorista.onibus = None
        if(removido.fiscal != None):
            removido.fiscal.onibus = None
    
    def deletar_fiscal(self, indice):
        removido = self.fiscais.pop(indice)
        if(removido.onibus != None):
            removido.onibus.fiscal = None

    def deletar_parada(self, indice):
        cod_parada = self.paradas[indice].codigo
        i_onibus = 0
        for onibus in self.onibus:
            if(onibus.paradas.count(cod_parada)>0):
                self.remover_parada_onibus(indice, i_onibus)
            i_onibus += 1
        self.paradas.pop(indice)

    def assignar_fiscal_onibus(self, i_fiscal, i_onibus):
        #Um teste deve ser realizado para desfazer o último vínculo entre fiscais e ônibus
        fiscal = self.fiscais[i_fiscal]
        onibus = self.onibus[i_onibus]
        if(fiscal.onibus != None):
            antigo_onibus = fiscal.onibus
            antigo_onibus.fiscal = None
        if(onibus.fiscal != None):
            antigo_fiscal = onibus.fiscal
            antigo_fiscal.onibus = None
        onibus.assignar_fiscal(fiscal)
        fiscal.assignar_onibus(onibus)

    def adicionar_parada_onibus(self, i_parada, i_onibus):
        cod_parada = self.paradas[i_parada].codigo
        onibus = self.onibus[i_onibus]
        if(onibus.paradas.count(cod_parada) == 0):
            onibus.paradas.append(cod_parada)
            onibus.atualiza_passagem()
        else:
            print("Erro! A rota do Ônibus já possui essa parada.")
    
    def remover_parada_onibus(self, i_parada, i_onibus):
        cod_parada = self.paradas[i_parada].codigo
        onibus = self.onibus[i_onibus]
        if(onibus.paradas.count(cod_parada) != 0):
            onibus.paradas.remove(cod_parada)
            onibus.atualiza_passagem()
        else:
            print("Erro! A rota do Ônibus não possui essa parada.")
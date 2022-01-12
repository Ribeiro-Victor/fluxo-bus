class Onibus:

    def __init__(self, codigo):
        self.codigo = codigo
        self.motorista = None
        self.fiscal = None
        self.paradas = []
        self.passagem = 0.0
        self.multiplicador_passagem = 0.5

    def __repr__(self):
        return (f"{str(self.codigo).center(10)}" + " | "
        f"{'N/A'.center(25) if self.motorista == None else self.motorista.nome.center(25)}" + " | "
        f"{'N/A'.center(25) if self.fiscal == None else self.fiscal.nome.center(25)}" + " | "
        f"{str(self.paradas).center(20)}" + " | "
        f"  R$ {self.passagem:.2f}" + "  |")

    def atualiza_passagem(self):
        self.passagem = self.multiplicador_passagem * len(self.paradas)
        


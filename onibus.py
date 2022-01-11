class Onibus:

    def __init__(self, codigo, motorista):
        self.codigo = codigo
        self.motorista = motorista
        self.fiscal = None
        self.paradas = []
        self.passagem = 0.0

    def __repr__(self):
        return (f"{str(self.codigo).center(10)}" + " | "
        f"{self.motorista.nome.center(25)}" + " | "
        f"{'N/A'.center(25) if self.fiscal == None else self.fiscal.nome.center(25)}" + " | "
        f"{str(self.paradas).center(20)}" + " | "
        f"  R$ {self.passagem:.2f}" + "  |")

    def atualiza_passagem(self):
        self.passagem = 0.5 * len(self.paradas)
        


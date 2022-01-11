class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome [0:25]
        self.idade = idade
        self.onibus = None

    def __repr__(self):
        return (f"{self.nome.center(25)}" + " | " 
        f"{str(self.idade).center(10)}" + " | "
        f"{'N/A'.center(20) if self.onibus == None else str(self.onibus.codigo).center(20)}" + " | ")



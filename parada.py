class Parada:
    def __init__(self, codigo, endereco):
        self.codigo = codigo
        self.endereco = endereco
    
    def __repr__(self):
        return (f"{str(self.codigo).center(10)}" + " | "
        f"{self.endereco.center(50)}" + " |")
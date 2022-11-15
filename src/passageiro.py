class Passageiro:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def ePrioridade(self):
        if self.idade >= 65:
            return True
        else:
            return False

    def getNome(self):
        return self.nome

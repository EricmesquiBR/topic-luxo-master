from src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.qtdNormal = capacidade - qtdPrioritarios
        self.passageirosNormal = []
        self.passageirosPrioritarios = []
        self.assentosPrioritarios = ['@'] * qtdPrioritarios
        self.assentosNormais = ['='] * (self.qtdNormal)
        self.assentos = '[' + ' '.join(self.assentosPrioritarios) + ' ' + ' '.join(self.assentosNormais) + ' ]'

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.qtdNormal

    def getPassageiroAssentoNormal(self, lugar):
        return self.passageirosNormal[lugar]

    def getPassageiroAssentoPrioritario(self, lugar):
        return self.passageirosPrioritarios[lugar]

    def getVagas(self):
        return self.qtdNormal + self.qtdPrioritarios

    def subir(self, passageiro: Passageiro):
        if self.getVagas() == 0:
            return False
        elif passageiro.ePrioridade() is True and self.qtdPrioritarios > 0:
            self.passageirosPrioritarios.append(passageiro)
            self.assentosPrioritarios[self.passageirosPrioritarios.index(passageiro)] = '@' + passageiro.getNome()
            self.assentos = '[' + ' '.join(self.assentosPrioritarios) + ' ' + ' '.join(self.assentosNormais) + ' ]'
            self.qtdPrioritarios -= 1

        elif passageiro.ePrioridade() is False and self.qtdNormal > 0:
            self.passageirosNormal.append(passageiro)
            self.assentosNormais[self.passageirosNormal.index(passageiro)] = '=' + passageiro.getNome()
            self.assentos = '[' + ' '.join(self.assentosPrioritarios) + ' ' + ' '.join(self.assentosNormais) + ' ]'
            self.qtdNormal -= 1

        elif passageiro.ePrioridade() is True and self.qtdPrioritarios == 0:
            if self.qtdNormal > 0:
                self.passageirosNormal.append(passageiro)
                self.assentosNormais[self.passageirosNormal.index(passageiro)] = '=' + passageiro.getNome()
                self.assentos = '[' + ' '.join(self.assentosPrioritarios) + ' ' + ' '.join(self.assentosNormais) + ' ]'
                self.qtdNormal -= 1

        elif passageiro.ePrioridade() is False and self.qtdNormal == 0:
            if self.qtdPrioritarios > 0:
                self.passageirosPrioritarios.append(passageiro)
                self.assentosPrioritarios[self.passageirosPrioritarios.index(passageiro)] = '@' + passageiro.getNome()
                self.assentos = '[' + ' '.join(self.assentosPrioritarios) + ' ' + ' '.join(self.assentosNormais) + ' ]'
                self.qtdPrioritarios -= 1

        return True

    def descer(self, nome):
        if nome in self.assentosPrioritarios:
            for i in range(len(self.passageirosPrioritarios)):
                if self.passageirosPrioritarios[i].getNome() == nome:
                    self.passageirosPrioritarios.pop(i)
                    self.assentosPrioritarios[i] = '@'
                    self.assentos = '[' + ' '.join(self.assentosPrioritarios)+' '+' '.join(self.assentosNormais) + ' ]'
                    self.qtdPrioritarios += 1
                    return True

        elif nome in self.assentosNormais:
            for i in range(len(self.passageirosNormal)):
                if self.passageirosNormal[i].getNome() == nome:
                    self.passageirosNormal.pop(i)
                    self.assentosNormais[i] = '='
                    self.assentos = '[' + ' '.join(self.assentosPrioritarios)+' '+' '.join(self.assentosNormais) + ' ]'
                    self.qtdNormal += 1
                    return True

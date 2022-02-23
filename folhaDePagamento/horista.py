from funcionario import Funcionario

class Horista(Funcionario):
    def __init__(self, id, nome, metodo_de_pagamento, sindicato, endereco, salario_hora):
        agenda_de_pagamento = "sexta"
        self.salario_hora = salario_hora
        Funcionario.__init__(self, id, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco)


    def exibir(self):
        Funcionario.exibir(self)
        print("Salario Hora: ", self.salario_hora)

    def pagamento(self):
        pagamento_total = 0
        for ponto in self.registro_de_ponto:
            hora = ponto[1] - ponto[0]
            if hora > 8:
                pagamento_total += (8 * self.salario_hora)
                hora -= 8
            pagamento_total += (hora * self.salario_hora)

        print("Pagando: ", pagamento_total - sum(self.taxas), " para o funcionario de id:", self.id)
        self.registro_de_ponto = []
        self.taxas = []

from funcionario import Funcionario

class Assalariado(Funcionario):
    def __init__(self, id, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco, salario):
        self.salario = salario
        Funcionario.__init__(self, id, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco)


    def exibir(self):
        Funcionario.exibir(self)
        print("Salario: ", self.salario)

    def pagamento(self):
        print("Pagando: ", self.salario - sum(self.taxas), " para o funcionario de id:", self.id)
        self.taxas = []

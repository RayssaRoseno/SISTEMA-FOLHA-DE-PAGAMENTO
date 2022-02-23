from assalariado import Assalariado

class Comissionado(Assalariado):
    def __init__(self, id, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco, salario, comissao):
        self.comissao = comissao
        Assalariado.__init__(self, id, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, salario, endereco)


    def exibir(self):
        Assalariado.exibir(self)
        print("Comissao: ", self.comissao)

    def pagamento(self):
        pagamento_total = self.salario
        for venda in self.registro_de_venda:
            pagamento_total += venda * (self.comissao/100)
        print("Pagando: ", pagamento_total - sum(self.taxas), " para o funcionario de id:", self.id)
        self.registro_de_venda = []
        self.taxas = []

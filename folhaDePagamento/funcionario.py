class Funcionario():

    def __init__(self, id, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco):
        self.nome = nome
        self.id = id
        self.metodo_de_pagamento = metodo_de_pagamento
        self.sindicato = sindicato
        self.agenda_de_pagamento =agenda_de_pagamento
        self.endereco = endereco
        self.registro_de_ponto = []
        self.registro_de_venda = []
        self.taxas = []

    def exibir(self):
        print("Nome: ", self.nome)
        print("ID: ", self.id)
        print("Metodo de pagamento: ", self.metodo_de_pagamento)
        if self.sindicato: participa = "Sim"
        else: participa = "Nao"
        print("Participa do sindicato: ", participa)
        print("Agenda de pagamento: ", self.agenda_de_pagamento )
        print("endereco: ", self.endereco )
        print("Registro de ponto: ", self.registro_de_ponto)
        print("Registro de venda: ", self.registro_de_venda)
        print("taxas: ", self.taxas)



    def adicionar_ponto(self, entrada, saida):
        self.registro_de_ponto.append((entrada, saida))

    def adicionar_venda(self, valor):
        self.registro_de_venda.append(valor)

    def adicionar_taxa(self, taxa):
        self.taxas.append(taxa)

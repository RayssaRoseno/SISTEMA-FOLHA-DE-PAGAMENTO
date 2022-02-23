from horista import Horista
from comissionado import Comissionado
from assalariado import Assalariado
import copy

class Facade():
    def __init__(self, taxa_de_sindicato = 100):
        self.id_atual = 0
        self.funcionarios = []
        self.agendas = {"mensal":[5], "semanal":[1,8,15,21], "bi-semanal": [15, 30], "sexta": [6, 12, 18, 24, 30]}
        self.dia_atual = 0
        self.estados = [self.copy()]
        self.taxa_de_sindicato = taxa_de_sindicato

    def copy(self):
        return copy.deepcopy(self)

    def adicionar_horista(self, nome, metodo_de_pagamento, endereco, sindicato, salario_hora):
        self.estados.append(self.copy())
        funcionario = Horista(self.id_atual, nome, metodo_de_pagamento, endereco, sindicato, salario_hora)
        self.funcionarios.append(funcionario)
        self.id_atual += 1
        funcionario.exibir()

    def adicionar_comissionado(self, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco, salario, comissao):
        self.estados.append(self.copy())
        funcionario = Comissionado(self.id_atual, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco, salario, comissao)
        self.funcionarios.append(funcionario)
        self.id_atual += 1
        funcionario.exibir()


    def adicionar_assalariado(self, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco, salario):
        self.estados.append(self.copy())
        funcionario = Assalariado(self.id_atual, nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco, salario)
        self.funcionarios.append(funcionario)
        self.id_atual += 1
        funcionario.exibir()

    def remover_funcionario(self, id):
        self.estados.append(self.copy())
        self.funcionarios[id] = None
        print("Funcionario de ID:", id, "Deletado")

    def adicionar_ponto(self, id, entrada, saida):
        self.estados.append(self.copy())
        self.funcionarios[id].adicionar_ponto(entrada, saida)

    def adicionar_venda(self, id, valor):
        self.estados.append(self.copy())
        self.funcionarios[id].adicionar_venda(valor)

    def adicionar_taxa(self, id, taxa):
        self.estados.append(self.copy())
        self.funcionarios[id].adicionar_taxa(taxa)

    def atualizar_dados(self, id, nome, endereco, metodo_de_pagamento, sindicato, agenda_de_pagamento):
        self.estados.append(self.copy())
        empregado_alterado = self.funcionarios[id]
        if nome: empregado_alterado.nome = nome
        if endereco: empregado_alterado.endereco = endereco
        if metodo_de_pagamento: empregado_alterado.metodo_de_pagamento = metodo_de_pagamento
        if sindicato: empregado_alterado.sindicato = sindicato
        if agenda_de_pagamento: empregado_alterado.dias_de_pagamento = agendas[agenda_de_pagamento]
        self.funcionarios[id] =  empregado_alterado
        self.funcionarios[id].exibir()


    def passar_dias(self, dias):
        self.estados.append(self.copy())
        for i in range(dias):
            self.dia_atual += 1
            self.dia_atual %= 31
            if self.dia_atual == 1:
                for funcionario in self.funcionarios:
                    if funcionario.sindicato:
                        funcionario.adicionar_taxa(self.taxa_de_sindicato)

            for funcionario in self.funcionarios:
                if self.dia_atual in self.agendas[funcionario.agenda_de_pagamento]:
                    funcionario.pagamento()

    def adicionar_taxas(self, id, valor):
        self.estados.append(self.copy())
        self.funcionarios[id].adicionar_taxa(valor)
        self.funcionarios[id].exibir()

    def adicionar_agenda(self, nome, dias_de_pagamento):
        self.agendas[nome_da_agenda] = dias_de_pagamento

    def desfazer(self):
        self = self.estados.pop()

    def get_nome_das_agendas(self):
        return self.agendas.keys()

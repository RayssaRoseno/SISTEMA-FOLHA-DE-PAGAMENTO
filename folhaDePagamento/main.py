from facade import Facade

sistema = Facade()

while True:
    entrada = int(input("Digite 0 para sair\nDigite 1 para adicionar um empregado\nDigite 2 para remover um empregado\nDigite 3 para adicionar um ponto ao funcionario\nDigite 4 para adicionar uma venda a um funcionario\nDigite 5 para adicionar uma taxa ao funcionario\nDigite 6 para alterar os dados de um funcionaro\nDigite 7 para passar os dias da folha de pagamento\nDigite 8 para criar uma nova agenda de pagamento\nDigite 9 para desfazer a ultima operacao"))

    if entrada == 0:
        exit(0)
    if entrada == 1:
        nome = input("Digite o nome do empregado: ")
        metodo_de_pagamento = input("Digite o metodo de pagemento: ")
        sindicato = input("O empregado é do sindicato: ")
        if sindicato.lower() == "sim":
            sindicato = True
        else: sindicato = False
        endereco = input("Digite o endereço do empregado: ")
        entrada = int(input("Digite 0 para adicionar assalariado\nDigite 1 para adicionar comissionado\nDigite 2 para adicionar Horista"))
        if entrada == 0:
            print("Agendas disponiveis: ", sistema.get_nome_das_agendas())
            agenda_de_pagamento = input("Digite a agenda de pagamento do funcionaro: ")
            salario = float(input("Salario"))
            sistema.adicionar_assalariado(nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco, salario)

        if entrada == 1:
            print("Agendas disponiveis: ", sistema.get_nome_das_agendas())
            agenda_de_pagamento = input("Digite a agenda de pagamento do funcionaro: ")
            salario = float(input("Salario"))
            comissao = float(input("Comissao (entre 0% a 100%)"))
            sistema.adicionar_comissionado(nome, metodo_de_pagamento, sindicato, agenda_de_pagamento, endereco, salario, comissao)

        if entrada == 2:
            salario = float(input("Salario Hora"))
            sistema.adicionar_horista(nome, metodo_de_pagamento, endereco, sindicato, salario)

    elif entrada == 2:
        id = int(input("Digite o ID do empregado: "))
        sistema.remover_funcionario(id)

    elif entrada == 3:
        id = int(input("Digite o ID do funcionario: "))
        entrada_ponto = float(input("Digite o horario de entrada: "))
        saida_ponto = float(input("Digite o horario de saida: "))
        sistema.adicionar_ponto(id, entrada_ponto, saida_ponto)

    elif entrada == 4:
        id = int(input("Digite o ID do funcionario: "))
        venda = float(input("Digite o valor da venda: "))
        sistema.adicionar_venda(id, venda)

    elif entrada == 5:
        id = int(input("Digite o ID do funcionario: "))
        taxa = float(input("Digite o valor da Taxa: "))
        sistema.adicionar_taxa(id, taxa)

    elif entrada == 6:
        id = int(input("Digite o ID do funcionario: "))
        print("Digite os novos dados do funcionario ou deixe em branco para manter o mesmo")
        nome = input("Digite o Nome do funcionario: ")
        endereco = input("Digite o endereço do funcionario: ")
        metodo_de_pagamento = input("Digite o metodo de pagamento do funcionario: ")
        sindicato = bool(input("Digite se o funcionario pertence ao sindicato: "))
        if sindicato.lower() == "sim":
            sindicato = True
        elif sindicato != "":
            sindicato = False
        agenda_de_pagamento = input("Digite agenda de pagemento: ")
        empregado_alterado = sistema.empregados[id]

    elif entrada == 7:
        dias = int(input("Quantos dias devem ser passados ?"))
        sistema.passar_dias(dias)

    elif entrada == 8:
        nome_da_agenda = input("Digite o nome da agenda")
        dias_de_pagamento = []
        while True:
            dia = int(input("adicione mais um dia de pagamento (ou um valor negativo para salvar os anteriores): "))
            if dia < 0: break
            else: dias_de_pagamento.append(dia)
        print("Nome da Agenda, dias de pagemento: ", dias_de_pagamento)
        sistema.adicionar_agenda(nome_da_agenda, dias_de_pagamento)

    elif entrada == 9:
        sistema.desfazer()

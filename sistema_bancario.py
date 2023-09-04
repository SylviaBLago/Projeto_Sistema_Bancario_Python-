saldo = 0
extrato = ""
LIMITE_SAQUE = 3
SAQUE_MAXIMO = 500
menu = """ 
    ########## BANCO SA #########
            1 - SAQUE
            2 - DEPOSITO
            3 - EXTRATO
            0 - SAIR
    #############################
"""

while True:

    opcao = int(input(menu))

    if opcao == 1: #opção saque

        print("##OPÇÃO SAQUE##")

        if LIMITE_SAQUE > 0:

            print(f"O saldo disponivel na sua conta é: R${saldo}")
            valor_saque = float(int(input("Qual o valor do saque?" )))
            
            if valor_saque > saldo:
                print("Esse valor não está disponível")
            
            elif valor_saque > SAQUE_MAXIMO:
                print("Esse valor ultrapassa o seu limite de saque")

            else:
                print("Retire o dinheiro na boca do caixa. Não esqueça de conferir o valor")
                saldo -= valor_saque
                print(f"O saldo atual da sua conta é R${saldo:.2f} \n")
                extrato += f"Saque: R$ {valor_saque:.2f} \n"
                LIMITE_SAQUE -= 1

        else:
            print("Você atingiu o seu limite de saques diários, tente novamente amanhã")   

    elif opcao == 2: #opção deposito
        print("##OPÇÃO DEPOSITO##")
        deposito = float(input("Qual valor você gostaria de depositar? "))

        if deposito > 0:
            saldo += deposito
            print(f"O saldo atual da sua conta é R${saldo:.2f} \n")
            extrato += f"Deposito de R${deposito:.2f} \n"

        else:
            print("#ERRO# \n O valor informado é invalido")

    elif opcao == 3: #opção extrato
        print("##########EXTRATO###########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("############################")
        
    elif opcao == 0: #opcão sair
        print("BANCO SA agradece sua parceria! \n Tenha um bom dia!")
        break
        
    else:
        print("Opção inválida! \n Selecione novamente a opção desejada")

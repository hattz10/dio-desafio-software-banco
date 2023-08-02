menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor do deposito: "))
        saldo += deposito
        deposito = str(deposito)
        extrato += "+R$" + deposito + "\n"

    elif opcao == "s":
        valor_saque = float(input("Qual valor deseja sacar: "))
        if valor_saque <= limite and numero_saques <= LIMITE_SAQUES and valor_saque <= saldo:
            print("Voce sacou: ", valor_saque)
            numero_saques += 1
            saldo -= valor_saque
            valor_saque = str(valor_saque)
            extrato += "-R$"+valor_saque + "\n"
        elif valor_saque > saldo:
            print("O valor que deseja sacar é maior que seu saldo")
        elif valor_saque > limite:
            print("O valor maximo de saque é de R$500.00")
        elif numero_saques > LIMITE_SAQUES:
            print("Você excedeu o limite de saques diarios")
    elif opcao == "e":
        print("Seu saldo atual é de: R$", saldo,
              "\nSuas movimentações foram\n", extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

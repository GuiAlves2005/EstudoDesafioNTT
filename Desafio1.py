class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.limite_saque = 500.00
        self.saques_diarios = 0
        self.limite_saques_diarios = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
            return
        if valor > self.limite_saque:
            print(f"Não é possível sacar mais que R$ {self.limite_saque:.2f} por vez.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        self.saldo -= valor
        self.saques.append(valor)
        self.saques_diarios += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato Bancário:")
            print("\nDepósitos:")
            for deposito in self.depositos:
                print(f"R$ {deposito:.2f}")
            print("\nSaques:")
            for saque in self.saques:
                print(f"R$ {saque:.2f}")
        print(f"\nSaldo Atual: R$ {self.saldo:.2f}")

# Função para interação com o usuário
def menu_banco():
    banco = Banco()
    while True:
        print("\nMenu Banco:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor para depósito: "))
            banco.depositar(valor)
        elif opcao == "2":
            valor = float(input("Informe o valor para saque: "))
            banco.sacar(valor)
        elif opcao == "3":
            banco.extrato()
        elif opcao == "4":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamando o menu interativo
menu_banco()

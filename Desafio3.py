class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao:
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        pass  # será implementado nas subclasses

class Deposito(Transacao):
    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito de R$ {self.valor:.2f}")

class Saque(Transacao):
    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque de R$ {self.valor:.2f}")
        else:
            print("Saldo insuficiente.")

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()

    def sacar(self, valor):
        saque = Saque(valor)
        saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = 3
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite de saques atingido.")
        elif valor > (self.saldo + self.limite):
            print("Limite insuficiente.")
        else:
            super().sacar(valor)
            self.numero_saques += 1

# Exemplo de uso
cliente = Cliente("João Silva", "Rua das Flores, 123")
conta_corrente = ContaCorrente(1, "0001", cliente, 500)
cliente.adicionar_conta(conta_corrente)

conta_corrente.depositar(1000)
conta_corrente.sacar(200)
conta_corrente.sacar(300)
conta_corrente.sacar(500)

print(f"Saldo final: R$ {conta_corrente.saldo:.2f}")
for transacao in conta_corrente.historico.transacoes:
    print(transacao)

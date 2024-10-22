import pickle

class Banco:
    def __init__(self):
        self.usuarios = self.carregar_usuarios()
        self.contas = []
        self.numero_conta = 1

    def salvar_usuarios(self):
        with open('usuarios.pkl', 'wb') as file:
            pickle.dump(self.usuarios, file)

    def carregar_usuarios(self):
        try:
            with open('usuarios.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        if any(usuario['cpf'] == cpf for usuario in self.usuarios):
            print("CPF já cadastrado.")
            return None
        usuario = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }
        self.usuarios.append(usuario)
        self.salvar_usuarios()
        print(f"Usuário {nome} criado com sucesso!")

    def criar_conta(self, cpf):
        usuario = next((u for u in self.usuarios if u['cpf'] == cpf), None)
        if not usuario:
            print("Usuário não encontrado.")
            return None
        conta = {
            "agencia": "0001",
            "numero_conta": self.numero_conta,
            "usuario": usuario
        }
        self.contas.append(conta)
        self.numero_conta += 1
        print(f"Conta criada com sucesso para {usuario['nome']} com número {self.numero_conta - 1}.")

    def exibir_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\nLista de Usuários Cadastrados:")
            for usuario in self.usuarios:
                print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Endereço: {usuario['endereco']}")
        print()

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    elif valor > limite:
        print(f"Não é possível sacar mais que R$ {limite:.2f} por vez.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("\nExtrato Bancário:")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")

def menu_banco():
    banco = Banco()
    saldo = 0
    extrato = []
    limite = 500.00
    numero_saques = 0
    limite_saques = 3

    while True:
        print("\nMenu Banco:")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Ver Usuários Cadastrados")
        print("4. Depositar")
        print("5. Sacar")
        print("6. Ver Extrato")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Informe o nome: ")
            data_nascimento = input("Informe a data de nascimento: ")
            cpf = input("Informe o CPF: ")
            endereco = input("Informe o endereço (logradouro, nro, bairro, cidade/sigla estado): ")
            banco.criar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == "2":
            cpf = input("Informe o CPF do usuário: ")
            banco.criar_conta(cpf)
        elif opcao == "3":
            banco.exibir_usuarios()
        elif opcao == "4":
            valor = float(input("Informe o valor para depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "5":
            valor = float(input("Informe o valor para saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
        elif opcao == "6":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "7":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamando o menu interativo
menu_banco()

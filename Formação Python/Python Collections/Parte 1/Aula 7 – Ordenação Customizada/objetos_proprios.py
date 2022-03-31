class ContaCorrente:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Conta de {self.nome}:\nCódigo: {self.codigo} Saldo: {self.saldo}'

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

conta_do_bruno = ContaCorrente('Bruno', 15)
conta_do_bruno.deposita(500)

conta_da_dani = ContaCorrente('Dani', 47685)
conta_da_dani.deposita(1000)

contas = [conta_da_dani, conta_do_bruno]

contas.insert(0,76)

print(contas[0], contas[1])
print()
deposita_para_todas(contas)
print(contas[0], contas[1])

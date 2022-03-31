from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, nome, codigo):
        self._nome = nome
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'Conta de {self._nome}:\nCódigo: {self._codigo} Saldo: {self._saldo}'


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo += 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

conta16 = ContaCorrente('Pedro', 16)
conta16.deposita(1000)
conta13 = ContaPoupanca('Vitor', 13)
conta13.deposita(1000)
# conta14 = ContaInvestimento('João', 14) Dará erro ao tentar executar

for conta in contas:
    conta.passa_o_mes()
    print(conta, '\n')


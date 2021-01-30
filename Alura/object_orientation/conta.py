class Conta:

    def __init__(self, numero, titular, saldo, limite=0):
        print("construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de R${self.__saldo:.2f} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print("Saque efetuado")
        else:
            print("Limite indisponivel")

    def transferir(self, valor, destino):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            destino.depositar(valor)
            print("Transferencia realizada")
        else:
            print("Limite indisponivel")

    @property
    def titular(self):
        return self.__titular.capitalize

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    def __pode_sacar(self, valor):
        limite_disponivel = self.__saldo + self.__limite
        return valor <= limite_disponivel

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

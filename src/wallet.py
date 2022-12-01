class BalanceInsuficiente(Exception):
    pass


class Wallet(object):
    def __init__(self, monto_ini=0):
        self.balance = monto_ini

    def gastar(self, monto_gasto):
        if self.balance < monto_gasto:
            raise BalanceInsuficiente(
              "No hay suficiente dinero para gastar"
            )
        self.balance -= monto_gasto

    def agregar(self, monto_agregado):
        self.balance += monto_agregado


class creditCard:

    def __init__(self, customer, bank, account, limit):
        """
        Create new credit card instance

        the initial balance is zero

        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

        def getCusomter(self):
            return self.bank

        def getAccount(self):
            return self._account

        def getBank(self):
            return self._bank

        def getBalance(self):
            return self._balance

        def charge(self, price):
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return true

        def makePayment(self, amount):
            self._balance -= amount


cc = creditCard('Luis Pena', '2nd bank', '1234 2123 1213 3221', 1000)

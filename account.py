from dataclasses import dataclass


class CurrencyConverter:
    def __init__(self):
        self.reference_currency = "EUR"
        self.exchange_rates = {"EUR": 1.0}

    def add_exchange_rate(self, currency, rate):
        self.exchange_rates[currency] = rate

    def get_exchange_rate(self, currency):
        if currency == self.reference_currency:
            return 1.0
        else:
            return self.exchange_rates[currency]

    def convert_to_eur(self, currency, amount):
        rate = self.get_exchange_rate(currency)
        return amount / rate

    def convert_from_eur(self, currency, amount):
        rate = self.get_exchange_rate(currency)
        return amount * rate


@dataclass
class Account:
    name: str
    currency: str
    balance: float = 0.0
    converter: CurrencyConverter = CurrencyConverter()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_balance_in_eur(self):
        return self.converter.convert_to_eur(self.currency, self.balance)

    def deposit_in_eur(self, amount):
        eur_amount = self.converter.convert_from_eur(self.currency, amount)
        self.deposit(eur_amount)

    def withdraw_in_eur(self, amount):
        eur_amount = self.converter.convert_from_eur(self.currency, amount)
        self.withdraw(eur_amount)

    def update_balance(self, balance):
        self.balance = balance

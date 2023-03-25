from dataclasses import dataclass
import datetime as dt


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


class Account:

    def __init__(self, name, currency, balance=0.0, converter=CurrencyConverter()):
        self.name = name
        self.currency = currency
        self.transactions = []  #
        self.balance = balance
        self.converter = converter

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

    def add_transaction(self, date, description, amount):

        new_balance = self.balance + amount

        # create new transaction dictionary and add it to the list of transactions
        transaction = {'date': date, 'description': description, 'amount': amount, 'balance': new_balance}
        self.transactions.append(transaction)

        # update balance
        self.balance = new_balance

    def get_transactions(self):
        return self.transactions


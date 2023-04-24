from dataclasses import dataclass
import datetime as dt


class CurrencyConverter:
    """
        Parameters:
            reference_currency: The base currency, that every other currency will be converted into.
            exchange_rates    : yes

        Functions:
            pass()
            __init__(self): initializes the class.
        
    """
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
        self.transactions = {}  #
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

    def _sort_transactions(self):
        if self.transactions:

            sorted_transaction_ids = sorted(self.transactions, key=lambda x: self.transactions[x]['date'])

            transactions_sorted = {}
            transactions = self.transactions.copy()
            for transaction_id in sorted_transaction_ids:
                transactions_sorted[transaction_id] = transactions[transaction_id]

            self.transactions = transactions_sorted

    def _update_transaction_balances(self):

        self._sort_transactions()
        current_balance = self.balance

        transaction_ids_reversed = sorted(self.transactions, reverse=True)

        updated_balance = current_balance
        for idx, transaction_id in enumerate(transaction_ids_reversed):

            self.transactions[transaction_id]['balance'] = updated_balance
            updated_balance -= self.transactions[transaction_ids_reversed[idx - 1]]['amount']



    def add_transaction(self, date, description, amount):

        new_balance = self.balance + amount

        # create new transaction dictionary and add it to the list of transactions
        transaction = {'date': date, 'description': description, 'amount': amount, 'balance': new_balance}
        try:
            trans_id = max(self.transactions.keys()) + 1
        except ValueError:
            trans_id = len(self.transactions)
        self.transactions[trans_id] = transaction

        # update balance
        self.update_balance(new_balance)

    def remove_transaction(self, trans_id):

        # update balance
        new_balance = self.balance - self.transactions[trans_id]['amount']
        self.update_balance(new_balance)

        # TODO: I have to somehow update balances properly in the history
        del self.transactions[trans_id]
        # update balance history
        self._update_transaction_balances()

    def get_transactions(self):
        return self.transactions


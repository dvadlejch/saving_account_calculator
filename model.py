from account import Account


class Model:

    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account):
        self.accounts[account.name] = account

    def get_account_balance(self, name):
        if name in self.accounts:
            return self.accounts[name].get_balance()
        else:
            return None

    def update_account_balance(self, name, balance):
        if name in self.accounts:
            try:
                self.accounts[name].update_balance(balance)
            except ValueError:
                print("Error: balance must be a number.")
        else:
            print("Error: account not found.")

    def remove_account(self, name):
        if name in self.accounts:
            del self.accounts[name]
        else:
            return None

    def get_all_accounts(self):
        return self.accounts

    def add_transaction(self, account_name, date, description, amount):
        if account_name in self.accounts:
            self.accounts[account_name].add_transaction(date, description, amount)

    def remove_transaction(self, account_name, trans_id):
        if account_name in self.accounts:
            self.accounts[account_name].remove_transaction(trans_id)

    def get_account_transactions(self, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name].get_transactions()
        return None



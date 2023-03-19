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



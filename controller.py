from view import View
from model import Model
from account import Account
import tkinter as tk
from datetime import date


class Controller:
    def __init__(self):
        """
        Initializes the Controller class by creating an instance of the View and Model classes.
        """
        try:
            self.view = View(self)
            self.model = Model()
        except Exception as e:
            print(f"Failed to initialize Controller: {e}")

        self.view.add_account_button.config(command=self.add_account)
        self.view.remove_account_button.config(command=self.remove_account)

        self.view.account_table.bind(
            "<Double-1>", lambda event: self.open_account_window()
        )

    def main(self):
        """
        Runs the main function of the View class to start the Account manager application.
        """
        try:
            self.view.main()
        except Exception as e:
            print(f"Failed to run main function: {e}")

    def handle_input(self, input):
        """
        Takes user input and updates the model accordingly.
        """
        try:
            # Handle user input here
            pass
        except Exception as e:
            print(f"Failed to handle input: {e}")

    def _add_account_to_model(self, name, currency, balance):
        try:
            account = Account(name=name, currency=currency, balance=balance)
            self.model.add_account(account)
        except Exception as e:
            print(f"Failed to add account: {e}")

    def add_account(self):
        """
        Creates an Account object with the given name, currency, and balance and adds it to the Model.
        """
        try:
            # get the user input from the entry fields
            account_name = self.view.account_name_entry.get()
            account_currency = self.view.account_currency_entry.get()
            balance = self.view.balance_entry.get()

            # validate the input
            if not account_name or not account_currency or not balance:
                self.view.show_error("All fields are required.")
                return

            try:
                balance = float(balance)
            except ValueError:
                self.view.show_error("Balance must be a number.")
                return

            self._add_account_to_model(account_name, account_currency, balance)
        except Exception as e:
            print(f"Failed to add account: {e}")

        # clear the entry fields
        self.view.account_name_entry.delete(0, tk.END)
        self.view.account_currency_entry.delete(0, tk.END)
        self.view.balance_entry.delete(0, tk.END)

        # update the table with the new account
        self.view.account_table.insert(
            "",
            "end",
            text=str(len(self.view.account_table.get_children()) + 1),
            values=(account_name, account_currency, balance),
        )

    def update_account_balance(self, name, balance):
        """
        Updates the balance of the Account with the given name in the Model.
        """
        try:
            self.model.update_account_balance(name, balance)
        except Exception as e:
            print(f"Failed to update account balance: {e}")

    def _remove_account_from_model(self, name):
        """
        Removes the Account with the given name from the Model.
        """
        try:
            self.model.remove_account(name)
        except Exception as e:
            print(f"Failed to remove account: {e}")

    def remove_account(self):
        """
        Removes the selected Account from the Model and the View.
        """
        try:
            # get the selected account from the table
            selection = self.view.account_table.selection()
            if not selection:
                self.view.show_error("Please select an account to remove.")
                return

            # get the name of the selected account
            name = self.view.account_table.item(selection)["values"][0]

            # remove the account from the model and the table
            self._remove_account_from_model(name)
            self.view.account_table.delete(selection)

            # update the numbering of the remaining accounts in the table
            for i, item in enumerate(self.view.account_table.get_children()):
                self.view.account_table.item(item, text=str(i + 1))

        except Exception as e:
            print(f"Failed to remove account: {e}")

    def get_account(self, name):
        accounts = self.model.get_all_accounts()
        if name in accounts:
            return accounts[name]
        return None

    def open_account_window(self):
        account_name = self.view.open_account_window()

        def add_trans():
            return self.add_transaction(account_name)

        self.view.add_transaction_button.config(command=add_trans)

        self._update_transactions_table(account_name=account_name)

    def _update_transactions_table(self, account_name):
        self.view.history_tables[account_name].delete(
            *self.view.history_tables[account_name].get_children()
        )

        transactions = self.model.get_account_transactions(account_name)
        for transaction_id, transaction in transactions.items():
            self.view.history_tables[account_name].insert(
                "",
                "end",
                text=str(
                    len(self.view.history_tables[account_name].get_children()) + 1
                ),
                values=(
                    transaction_id,
                    transaction["date"],
                    transaction["description"],
                    transaction["amount"],
                    transaction["balance"],
                ),
            )

    def _update_account_table(self, account_name):
        account_table_itm = self.view.account_table.get_children()
        for acc_table_id in account_table_itm:
            acc_values = self.view.account_table.item(acc_table_id)["values"]
            if acc_values[0] == account_name:
                values_new = acc_values.copy()
                values_new[2] = self.model.get_account_balance(name=account_name)
                self.view.account_table.item(
                    acc_table_id,
                    values=values_new,
                )

    def add_transaction(self, account_name):
        self.model.add_transaction(
            account_name=account_name,
            date=date(2000, 10, 15),
            description="test",
            amount=200,
        )

        self._update_transactions_table(account_name=account_name)

        self._update_account_table(account_name=account_name)

    def remove_transaction(self, account_name, transaction_id):
        self.model.remove_transaction(
            account_name=account_name, trans_id=transaction_id
        )
        self._update_transactions_table(account_name)
        self._update_account_table(account_name)


if __name__ == "__main__":
    app_manager = Controller()
    app_manager.main()

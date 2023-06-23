import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk

import matplotlib.pyplot as plt


class View(tk.Tk):
    """
    Represents the graphical user interface (GUI) of the account manager application.

    Attributes:
        PAD (int): The padding size for the main frame.
        balance_entry (tk.Entry): The entry field for the account balance.
        interest_entry (tk.Entry): The entry field for the interest rate.
        calculate_button (ttk.Button): The button used to calculate the interest.
        dummy_button (ttk.Button): A placeholder button for testing.
        listbox (tk.Listbox): The listbox for displaying account transactions.
        _main_frame (ttk.Frame): The main frame of the GUI.
        _status_bar (tk.Label): The status bar at the bottom of the GUI.

    Methods:
        main(): Runs the main event loop of the GUI.
        set_status_text(text: str): Sets the text of the status bar.
    """

    PAD = 10

    def __init__(self, controller):
        """Initialize the main window of the application.

        This method creates the main window with a fixed size and a menu bar, a main frame with several widgets
        (entry fields, buttons, listbox, etc.), and a status bar at the bottom. The widgets are positioned using the
        grid layout manager.
        """
        super().__init__()

        self.title("Account manager")
        self.controller = controller
        self.geometry("1200x800")  # set a fixed window size
        self._make_menu_bar()  # add a menu bar
        self._make_main_frame()
        self._make_status_bar()  # add a status bar

        self._open_windows = {}
        self.history_tables = {}

    def main(self):
        self.mainloop()

    def _make_menu_bar(self):
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

    def show_context_menu(self, event):
        """
        Displays the right-click context menu at the cursor location.
        """
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def _make_main_frame(self):
        self._main_frame = ttk.Frame(self)
        self._main_frame.pack(padx=self.PAD, pady=self.PAD)

        self.account_name_entry = self._make_entry(
            parent_frame=self._main_frame,
            label_text="Account Name:",
            row=0,
            column=2,
        )

        self.account_currency_entry = self._make_entry(
            parent_frame=self._main_frame,
            label_text="Account Currency:",
            row=1,
            column=2,
        )

        self.balance_entry = self._make_entry(
            parent_frame=self._main_frame,
            label_text="Account Balance:",
            row=2,
            column=2,
        )

        self.add_account_button = self._make_button(
            parent_frame=self._main_frame,
            text="Add account",
            command=self._dummy_func,
            row=0,
            column=1,
        )

        self.remove_account_button = self._make_button(
            parent_frame=self._main_frame,
            text="Remove account",
            command=self._dummy_func,
            row=1,
            column=1,
        )

        # create an listbox
        # self.listbox = self._make_listbox(
        #     parent_frame=self._main_frame,
        #     row=5,
        #     column=0
        # )

        # create an accounts table
        self.account_table = self._make_account_table(
            parent_frame=self._main_frame, row=3, column=0
        )
        # self.account_table.bind("<Double-1>", lambda event: self._open_account_window())

    def open_account_window(self):
        return self._open_account_window()

    def _open_account_window(self):
        # self.new_window.geometry("400x400")

        selected_account_data = self.account_table.item(
            self.account_table.selection()[0]
        )
        account_name = selected_account_data["values"][0]

        if account_name not in self._open_windows.keys():
            self._open_windows[account_name] = tk.Toplevel(self._main_frame)
            self._open_windows[account_name].title(account_name)

            # properly close the window when it's closed by the user
            self._open_windows[account_name].protocol(
                "WM_DELETE_WINDOW",
                lambda: self.close_account_window(account_name=account_name),
            )

            self.history_tables[account_name] = self._make_history_table(
                parent_frame=self._open_windows[account_name],
                row=4,
                column=0,
            )

            # Bind the right-click event to the account history table
            self.history_tables[account_name].bind("<Button-3>", self.show_context_menu)

            self.add_transaction_button = self._make_button(
                parent_frame=self._open_windows[account_name],
                text="add transaction",
                command=None,
                row=0,
                column=0,
            )
        else:
            self._open_windows[account_name].lift()

        # Create the right-click context menu
        self.context_menu = tk.Menu(self.account_table, tearoff=0)
        self.context_menu.add_separator()

        self.context_menu.add_command(
            label="remove transaction",
            command=lambda: self._remove_transaction_from_history_table(
                account_name=account_name
            ),
        )

        return account_name

    def close_account_window(self, account_name):
        return self._close_account_window(account_name)

    def _close_account_window(self, account_name):
        self._open_windows[account_name].destroy()
        del self._open_windows[account_name]

    def _remove_transaction_from_history_table(self, account_name):
        # TODO: IndexError: tuple index out of range fix this
        selected_transaction_data = self.history_tables[account_name].item(
            self.history_tables[account_name].selection()[0]
        )

        trans_id = selected_transaction_data["values"][0]
        self.controller.remove_transaction(
            account_name=account_name, transaction_id=trans_id
        )

    def _make_status_bar(self):
        self._status_bar = tk.Label(
            self, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self._status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_status_text(self, text):
        self._status_bar.config(text=text)

    def _make_entry(self, parent_frame, label_text, row, column):
        # create a label for the entry field
        label = ttk.Label(parent_frame, text=label_text)
        label.grid(column=column, row=row, sticky=tk.W)

        # create the entry field
        entry = tk.Entry(parent_frame)
        entry.grid(column=column + 1, row=row)

        # return the entry field
        return entry

    def _make_button(self, parent_frame, text, command, row, column):
        """Creates a ttk.Button widget with the specified text and command, and places it in the main frame at the
        specified row and column positions.

        :param: parent_frame:  The parent frame where the button should be created.
        :param text: The text to be displayed on the button.
        :param command: The function to be called when the button is clicked.
        :param row: The row position for the button in the main frame.
        :param column: The column position for the button in the main frame.
        :return: ttk.Button: The created button widget.
        """

        # create the button
        button = ttk.Button(parent_frame, text=text, command=command)
        button.grid(column=column, row=row, pady=5)

        # return the button
        return button

    def _make_listbox(self, parent_frame, row, column):
        """Creates a ttk.Listbox widget and places it in the specified parent frame at
        the specified row and column positions.

        :param parent_frame: The parent frame where the listbox should be created.
        :param row: The row position for the listbox in the parent frame.
        :param column: The column position for the listbox in the parent frame.
        :return: ttk.Listbox: The created listbox widget.
        """

        lb = tk.Listbox(parent_frame)
        lb.grid(row=row, column=column)
        return lb

    def _make_account_table(self, parent_frame, row, column):
        """
        Creates a ttk.Treeview widget and places it in the specified parent frame at
        the specified row and column positions.

        Args:
            parent_frame (tk.Frame): The parent frame where the treeview should be created.
            row (int): The row position for the treeview in the parent frame.
            column (int): The column position for the treeview in the parent frame.

        Returns:
            ttk.Treeview: The created treeview widget.
        """
        tr = ttk.Treeview(parent_frame, columns=("Name", "Currency", "Balance"))
        tr.heading("Name", text="Name")
        tr.heading("Currency", text="Currency")
        tr.heading("Balance", text="Balance")
        tr.grid(row=row, column=column)
        return tr

    def _make_history_table(self, parent_frame, row, column):
        tr = ttk.Treeview(
            parent_frame, columns=("ID", "Date", "Description", "Amount", "Balance")
        )
        tr.heading("ID", text="transaction ID")
        tr.heading("Date", text="Date")
        tr.heading("Description", text="Description")
        tr.heading("Amount", text="Amount")
        tr.heading("Balance", text="Balance")
        tr.grid(row=row, column=column)
        return tr

    def _make_graph(self):
        """Creates a simple line graph using Matplotlib.

        :return:
            None
        """
        plt.plot([0, 1, 2, 3], [0, 1, 4, 9], ".")
        plt.show()

    def show_message(self, message):
        messagebox.showinfo("Message", message)

    def show_error(self, error):
        messagebox.showerror("Error", error)

    def _dummy_func(self):
        print("I am a dummy function!")

# saving_account_calculator

This will be an amazing program.

Parts of the program:
- GUI
- Data Base
- Live Exchange Rate Data
- Account management
- Account history

User stories:
- User can create accounts.
- User can delete accounts.
- User can oversee already created accounts.
- User can save account data.
- *User can modify account data? (name, amount?, description, bankname)*
- Accounts store information about past transactions.
- Accounts store {username, currency, amount, transactions, description, bankname}
- User can add transactions.
- User can delete transactions.
- User can read current time exchange rates.
- User can read account data from a plot, such as: {amount}
- User can read sum of money data from a plot.
 
It would be also good, if transactions could be gathered into groups. For example, transfer fee. User can check, how much money does he or she spend on transactions.

---

## GUI High Level Design

In all of the GUI windows, the following informations should be visible:
  - current date
  - save file name (if available)
  - account name (if available)
  
1. **Select Save File window**

	GUI lists found Saved Files in a drop-down menu.  
	User can select one, open selected, create new or delete.  
	Buttons: open, create new, delete selected.  
	1. *Open*: if Saved File is selected, load selected save file, else error message: "No saved file selected!". If Saved File is loaded successfully navigate to "Main window" window, else error message "Saved File could not be loaded".
	2. *Create new*: create new. Don't load any saved file. Pop-up save window (to select save location), if save is successful: navigate to (empty) "Main window" window, else error message: "Could not create new file!".
	3. *Delete selected*: if Saved File is selected, delete selected saved file. Else error message: "No saved file selected!". User stays in this window.
 
2. **Main window**

	All the accounts are listed with values: account name, currency, balance.  
	User can create, select and delete Accounts.  
	User can navigate back to "Select Save File" window to load different user.  
	(Optional: the last 3-5 transactions could be listed with information: Account Name, Currency, Amount, Transaction Type.)  
	1. *Select Account*: if Account is selected, load selected account, else error message: "No accunt selected!". If Account is loaded successfully, navigate to "Account Overview" window, else error message "Account could not be opened".
	2. *Create Account*: navigate to "Account Creation" window.
	3. *Delete Account*: if Account is selected, delete selected Account (don't forget transactions). Else error message: "No account selected!". User stays in this window.
	4. *Close*: navigate to Select Save File window.
  
3. **Account Creation**

	User needs to enter values into input fields. Variables should be around sombewhere in this "documentation".  
	1. *Create*: If all required input fields have VALID data, create new account, save data. Else error message: "Please enter all necessary data!" with inline error message at left out input fields. If saving is successful,navigate to "Account Overview" window of the new account. Else error message: "Account could not be created!"
	2. *Cancel*: Navigate to "Main Window".

4. **Account Overview**

	All transactions belonging to the account are listed in a scroll-down menu, or with a page-turning flip-book style (to be decided).  
	Transactions include account names (sender, receiver), amount, currency, (Optional: transaction rate at time of sending (we need to keep in mind, it is not the same as the time of booking)), sent or received (can be color coded too, since this information is deductable from sender/receiver).  
	A nice plot of money vs time. Maybe info abount inflation of the Account currency?  
	Informations are listed: Account Name, Currency, Amount, Additional info (comments, descriptions, notes, etc.).  
	User can add, select (modify?) or delete transactions. User can modify Account data. User can return to "Main Window".  
	1. *Select Transaction*: I don't think navigation is necessary, maybe a drop-down thingie that holds extra info. So what I mean is, the fields, containing the transactions in the list are expandable.
	2. *Ass Transaction*: Navigate to "Transaction Creation" page. Maybe pop-up? But we need to refresh the page anyway (except for cancellation).
	3. *Delete Transaction*: If transaction is selected, delete it. Else, error message: "No transaction selected!". If deletion is successful, reload page. Else error message "Transaction could not be deleted!".
	4. *Modify Account data*: navigates to "Account Edit" window (or could be merged with "Account Creation" window?).
	5. *Return*: Navigate to "Main Window".
  
5. **Transaction Creation**

	User needs to enter values into input fields. Variables should be around sombewhere in this "documentation". Timestamp?  
	1. *Add Transaction*: If all required input fields have VALID data, create transaction, save data, attach to selected account. Else error message: "Please enter all necessary data!" with inline error message at left out input fields. If saving is successful,navigate to "Account Overview" window of the account. Else error message: "Transaction could not be added!"
	2. *Cancel*: Navigate to "Account Overview" of the account.


6. **Account Edit**

	Basically the same, as the "Account Creation" window.  
	Data to the input fields is already filled, User can modify.  
	1. *Save*: If all required input fields have VALID data, save account data. Else error message: "Please enter all necessary data!" with inline error message at left out input fields. If saving is successful,navigate to "Account Overview" window of the account. Else error message: "Account could not be created!"
	2. *Cancel*: Navigate to "Account Overview".


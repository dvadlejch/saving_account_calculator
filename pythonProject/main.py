import tkinter as tk
import GUI as gui

'''
================================================================================================
| IMPORTANT!!!!
| VERY RECENT!!!!
|
| FOR GEOMETRY (PLACING WIDGETS (FRAMES)) YOU SHOULD NOW USE GRID COMMAND INDSTEAD OF PACK!!
| USE .grid() INSTEAD OF .pack() !!!!!!
================================================================================================

What could be a good idea, to be made into a separate module?

Infobox?
This way it could become more complex. Probably there's already a module that
does this, we just need to decide what would be good for error logging. But we can
also make one inhouse.
Pros:
 + All the subsystems could use it (GUI, Account Manager, Data Manager)
 + Umm... more nice?
Cons:
 - ?

All the pages could be made into one class, so it's easier to maintain.
The GUI imports them all, and uses them accordingly. More readable code?
But I'm not sure about this one.
 + It could make sense. Right now one page contains only one Frame (3, if
   counting Menubar and Infobox). But as the GUI gets more complex,
   it could be worth it to separate things to logical units.
How to separate all these things?
A GUI page lifecycle:
 1./ Initialize: create Frame, create components withing Frame, pack components.
 2./ Load Frame (Frame.pack)
 3./ Clear Frame (Frame.forget)
The GUI only needs to access these three functions, the Pages can handle everything else
within. The transition from Page-A to Page-B would look like:
def transition_A_B():
    A.forget_all()
    B.pack_all()
    # Infobox? If it's fixated at bottom, I guess it's cool, but idk
    
WROOOOOOOOOOOOOOOOOONG
GUI needs MORE!!!
 - The transition initiating buttons on the Pages need the transition functions of the GUI!!!!
 - Is this really more readable code???!!!
 - So when initializing the Page object, the GUI needs to pass on:
    - Root
    - Transition functions (usually 3, back, select, create new)

...nooooooooooooooooooo hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
So, what if
GUI needs:
 - to enter a callback function
 - and maybe a variable (list), to store information in.
 - and the GUI will act as a state machine, and the buttons manipulate bits in the state machine.

'''

#
# # Why the class????!!!!
# # GUI variables
# # Because I'm sick and tired of not being able to
# # reach out of scope variables from functions.
# # scope scope scope scope scope v
# class GUI_variables:
#     message_list = [""] * 5
#     message_list_enabled = True
# # Commands
#
# # General
#
#
# def send_message(msg):
#     GUI_variables.message_list.pop()
#     GUI_variables.message_list.insert(0, msg)
#     # print(GUI_variables.message_list)
#     # Why would you even do such a thing
#     infobox_frame.forget()
#     infobox_label_1.config(text=GUI_variables.message_list[0])
#     infobox_label_2.config(text=GUI_variables.message_list[1])
#     infobox_label_3.config(text=GUI_variables.message_list[2])
#     infobox_label_4.config(text=GUI_variables.message_list[3])
#     infobox_label_5.config(text=GUI_variables.message_list[4])
#     if GUI_variables.message_list_enabled:
#         infobox_frame.pack(side=BOTTOM, anchor=W, padx=10, pady=10, fill=X)
#
# def toggle_message_list():
#     GUI_variables.message_list_enabled = not GUI_variables.message_list_enabled
#     if GUI_variables.message_list_enabled:
#         send_message("Info: Infobox enabled.")
#     else:
#         infobox_frame.forget()
#
# # select_save_file_window
#
#
# def select_save_file_open_saved_file():
#     msg = "Open saved file command selected."
#     print(msg)
#     send_message("Info: " + msg)
#     # TODO
#     # a dummy open saved file window shall open. Here the user can select only two options:
#     # FAIL or SUCCESS, to simulate behavior. All windows must operate with dummy data.
#
#     def transition_select_saved_file_to_main_window():
#         select_save_file_frame.forget()
#         # TODO
#         # Open new window
#         main_window_frame.pack()
#         # no need for infobox_frame.pack()
#         # it is already done in send_message()
#         msg_i = "Main Window entered."
#         print(msg_i)
#         send_message("Info: " + msg_i)
#         dummy_confirmation_window.destroy()
#
#     def transition_failure():
#         msg_i = "File could not be opened."
#         print(msg_i)
#         send_message("Error: " + msg_i)
#         dummy_confirmation_window.destroy()
#
#     dummy_confirmation_window = Tk()
#     dummy_confirmation_window.title("Open saved file")
#     dummy_confirmation_window.geometry("400x100")
#     dummy_confirmation_window_frame = Frame(dummy_confirmation_window)
#     dummy_confirmation_window_label = Label(dummy_confirmation_window_frame,
#                                             text="Load previously saved file. Is load successful?")
#     dummy_confirmation_window_ack_btn = Button(dummy_confirmation_window_frame,
#                                                width=10,
#                                                pady=10,
#                                                padx=10,
#                                                text="YES",
#                                                command=transition_select_saved_file_to_main_window
#                                                )
#     dummy_confirmation_window_ref_btn = Button(dummy_confirmation_window_frame,
#                                                width=10,
#                                                pady=10,
#                                                padx=10,
#                                                text="NO",
#                                                command=transition_failure
#                                                )
#     dummy_confirmation_window_label.pack()
#     dummy_confirmation_window_ack_btn.pack(side="left")
#     dummy_confirmation_window_ref_btn.pack(side="right")
#     dummy_confirmation_window_frame.pack()
#
#
# # def select_save_file_create_new_file():
# #     msg = "Create new save file command selected."
# #     print(msg)
# #     send_message("Info: " + msg)
# #     # TODO
# #     # a dummy create new file window shall open. Here the user can select only two options:
# #     # FAIL or SUCCESS, to simulate behavior. All windows must operate with dummy data.
# #
# #     def transition_select_saved_file_to_main_window():
# #         select_save_file_frame.forget()
# #         # TODO
# #         # Open new window
# #         main_window_frame.pack()
# #         # no need for infobox_frame.pack()
# #         # it is already done in send_message()
# #         msg_i = "Main Window entered."
# #         print(msg_i)
# #         send_message("Info: " + msg_i)
# #
# #         dummy_confirmation_window.destroy()
# #
# #     def transition_failure():
# #         msg_i = "File could not be created."
# #         print(msg_i)
# #         send_message("Error: " + msg_i)
# #
# #         dummy_confirmation_window.destroy()
# #
# #     dummy_confirmation_window = Tk()
# #     dummy_confirmation_window.title("Create new file")
# #     dummy_confirmation_window.geometry("400x100")
# #     dummy_confirmation_window_frame = Frame(dummy_confirmation_window)
# #     dummy_confirmation_window_label = Label(dummy_confirmation_window_frame,
# #                                             text="Create new save file. Is the creation successful?"
# #                                             )
# #     dummy_confirmation_window_ack_btn = Button(dummy_confirmation_window_frame,
# #                                                width=10,
# #                                                pady=10,
# #                                                padx=10,
# #                                                text="YES",
# #                                                command=transition_select_saved_file_to_main_window
# #                                                )
# #     dummy_confirmation_window_ref_btn = Button(dummy_confirmation_window_frame,
# #                                                width=10,
# #                                                pady=10,
# #                                                padx=10,
# #                                                text="NO",
# #                                                command=transition_failure
# #                                                )
# #     dummy_confirmation_window_label.pack()
# #     dummy_confirmation_window_ack_btn.pack(side="left")
# #     dummy_confirmation_window_ref_btn.pack(side="right")
# #     dummy_confirmation_window_frame.pack()
#
#
# # def select_save_file_delete_file():
# #     msg = "Delete file command selected."
# #     print(msg)
# #     send_message("Info: " + msg)
#
#
# def show_home():
#     select_save_file_frame.pack()
#     infobox_frame.pack()
#
#     msg = "Select Save File window entered."
#     print(msg)
#     send_message("Info: " + msg)
#
# def main_window_select_account():
#
#     msg = "Open selected account."
#     print(msg)
#     send_message("Info: " + msg)
#
# def main_window_create_account():
#
#     msg = "Create new account."
#     print(msg)
#     send_message("Info: " + msg)
#
# def main_window_close():
#     main_window_frame.forget()
#     select_save_file_frame.pack()
#     # infobox_frame.pack()
#     # no need for infobox_frame.pack
#     # it is already done in send_message function
#     msg = "Select Save File window entered."
#     print(msg)
#     send_message("Info: " + msg)
#
# def main_window_delete_account():
#     msg = "'Selected' Account deleted."
#     print(msg)
#     send_message("Info: " + msg)
#
# def quit_application():
#     root.quit()

# # Root
# root = tk.Tk()
# root.title("Your Money")
# root.geometry("300x500")

# # Build select_save_file_window
# # select_save_file_frame = Frame(root)
# # select_save_file_label = Label(select_save_file_frame, text="Select Save File")
# # select_save_file_open_button = Button(select_save_file_frame,
# #                                       text="Open saved file",
# #                                       command=select_save_file_open_saved_file
# #                                       )
# # select_save_file_create_button = Button(select_save_file_frame,
# #                                         text="Create new file",
# #                                         command=select_save_file_create_new_file
# #                                         )
# # select_save_file_delete_button = Button(select_save_file_frame,
# #                                         text="Delete file",
# #                                         command=select_save_file_delete_file
# #                                         )
# #
# # select_save_file_label.pack()
# # select_save_file_open_button.pack()
# # select_save_file_create_button.pack()
# # select_save_file_delete_button.pack()
#
# # Build main_window
# main_window_frame = Frame(root)
# main_window_label = Label(main_window_frame, text="Main Window")
# main_window_account_list_dummy = Label(main_window_frame, text="Imagine all the accounts here...", bg="white")
# main_window_select_account_button = Button(main_window_frame, text="Select Account",command=main_window_select_account)
# main_window_create_account_button = Button(main_window_frame, text="Create Account", command=main_window_create_account)
# main_window_delete_account_button = Button(main_window_frame, text="Delete Account", command=main_window_delete_account)
# main_window_close_button = Button(main_window_frame, text="Close", command=main_window_close)
#
# main_window_account_list_dummy.pack()
# main_window_select_account_button.pack()
# main_window_create_account_button.pack()
# main_window_delete_account_button.pack()
# main_window_close_button.pack()
# # Build account_overview_window
# # Build account_creation_window
# # Build account_edit_window
# # Build transaction_creation_window
#
# # Infobox
# infobox_frame = Frame(root, background="black", padx=1, pady=1)
# infobox_label_1 = Label(infobox_frame, text=GUI_variables.message_list[0], anchor="w")
# infobox_label_2 = Label(infobox_frame, text=GUI_variables.message_list[1], anchor="w")
# infobox_label_3 = Label(infobox_frame, text=GUI_variables.message_list[2], anchor="w")
# infobox_label_4 = Label(infobox_frame, text=GUI_variables.message_list[3], anchor="w")
# infobox_label_5 = Label(infobox_frame, text=GUI_variables.message_list[4], anchor="w")
#
# infobox_label_1.pack(fill="x")
# infobox_label_2.pack(fill="x")
# infobox_label_3.pack(fill="x")
# infobox_label_4.pack(fill="x")
# infobox_label_5.pack(fill="x")
#
# # Menubar
# bottom_frame = Frame(root, relief="raised", borderwidth=1)
# message_list_button = Button(bottom_frame, text="Log", command=toggle_message_list, bg="blue", fg="white", font="bold")
# quit_button = Button(bottom_frame, text="Quit", command=quit_application, bg="red", fg="white", font="bold")
#
# quit_button.pack(side=RIGHT, padx=10, pady=5)
# message_list_button.pack(side=RIGHT, padx=10, pady=5)
# bottom_frame.pack(side=BOTTOM, fill=X)
#
# # Initially show the home frame
# show_home()
# Start
# root.mainloop()

theGUI = gui.GUI.GUI()
theGUI.start()
theGUI.root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

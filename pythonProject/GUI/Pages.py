from abc import ABC, abstractmethod
import tkinter as tk

'''
Abstract class for all pages.
'''


class Page(ABC):

    def __init__(self, callback):
        self.callback = callback

    # Function responsible for loading all Frames within Page.
    @abstractmethod
    def pack_all(self):
        pass

    # Function responsible for clearing all Frames within Page.
    @abstractmethod
    def forget_all(self):
        pass

'''
Frames:
    Right now there is only one frame: frame. This contains all elements.
    In the future, this might change.
'''
class SSFWindow(Page):

    def __init__(self, root, callback):
        Page.__init__(self,callback)
        # Build select_save_file_window
        self.frame = tk.Frame(root, pady=10, padx=10)
        self.label = tk.Label(self.frame, text="Select Save File")
        self.open_button = tk.Button(self.frame, text="Open saved file", command=self.open_saved_file)
        self.create_button = tk.Button(self.frame, text="Create new file", command=self.create_new_file)
        self.delete_button = tk.Button(self.frame, text="Delete file", command=self.delete_file)
        # Pack all
        self.label.pack()
        self.open_button.pack()
        self.create_button.pack()
        self.delete_button.pack()

    def pack_all(self):
        self.frame.pack(side=tk.LEFT)

    def forget_all(self):
        self.frame.forget()

    def delete_file(self):
        msg = "Delete file command selected."
        self.callback(msg)
        # TODO: Infobox class
        # send_message("Info: " + msg)

    def create_new_file(self):
        msg = "Create new save file command selected."
        self.callback(msg)
        # TODO: Infobox class
        # send_message("Info: " + msg)

        # Removed, because transition is the task of GUI!
        # But how... How will the GUI know, what transition to do...
        #
        # # def transition_select_saved_file_to_main_window():
        # #     select_save_file_frame.forget()
        # #     # TODO
        # #     # Open new window
        # #     main_window_frame.pack()
        # #     # no need for infobox_frame.pack()
        # #     # it is already done in send_message()
        # #     msg_i = "Main Window entered."
        # #     print(msg_i)
        # #     send_message("Info: " + msg_i)
        # #
        # #     dummy_confirmation_window.destroy()
        #
        # def transition_failure():
        #     msg_i = "File could not be created."
        #     print(msg_i)
        #     send_message("Error: " + msg_i)
        #
        #     dummy_confirmation_window.destroy()
        #
        # dummy_confirmation_window = Tk()
        # dummy_confirmation_window.title("Create new file")
        # dummy_confirmation_window.geometry("400x100")
        # dummy_confirmation_window_frame = Frame(dummy_confirmation_window)
        # dummy_confirmation_window_label = Label(dummy_confirmation_window_frame,
        #                                         text="Create new save file. Is the creation successful?"
        #                                         )
        # dummy_confirmation_window_ack_btn = Button(dummy_confirmation_window_frame,
        #                                            width=10,
        #                                            pady=10,
        #                                            padx=10,
        #                                            text="YES",
        #                                            command=transition_select_saved_file_to_main_window
        #                                            )
        # dummy_confirmation_window_ref_btn = Button(dummy_confirmation_window_frame,
        #                                            width=10,
        #                                            pady=10,
        #                                            padx=10,
        #                                            text="NO",
        #                                            command=transition_failure
        #                                            )
        # dummy_confirmation_window_label.pack()
        # dummy_confirmation_window_ack_btn.pack(side="left")
        # dummy_confirmation_window_ref_btn.pack(side="right")
        # dummy_confirmation_window_frame.pack()

    def open_saved_file(self):
        msg = "Open saved file command selected."
        self.callback(msg)
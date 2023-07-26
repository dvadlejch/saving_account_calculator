import tkinter as tk
import GUI.Pages as p

def gui_test():
    print("GUI test! This function is defined in GUI.py!")

class GUI():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x300")
        self.select_saved_file_window = p.SSFWindow(self.root,self.gui_callback)

    def gui_callback(self, message):
        # buttons will trigger this function
        print("Callback called with value [", message, "]")
        # In theory, what right now seems like not a completely insane
        # option, is that the 'message' variable will contain the code
        # based on which the callback function will decide which transition
        # is needed.

    def start(self):
        self.select_saved_file_window.pack_all()
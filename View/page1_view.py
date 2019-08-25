import tkinter as tk


class Page1View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent, submit_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=1500, height=1200)
        self._parent = parent
        self._submit_callback = submit_callback
        self._create_widgets()
        self._managers = []

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """
        self._label = tk.Label(self, text="Managers")
        self._label.grid(row=1,column=0,padx=20)
        self._listbox = tk.Listbox(self,height=20,width=40)
        self._listbox.grid(row=2, column=0, padx=50)

        self._button = tk.Button(self,
                                 text="refresh",
                                 command=self._submit_callback)
        self._button.grid(row=4,column=0,padx=20)

    def get_form_data(self, managers):
        """ Retrieve and save player data and insert into list"""
        self._listbox.delete(0, tk.END)
        print(managers)
        for manager in managers:
            self._listbox.insert(tk.END, '%s %s(%s) - %s' % (manager['f_name'], manager['l_name'], manager['id'],
                                                             manager['manager_position']))
        self._managers = managers

    def selected_item(self):
        """ return the currently selected player"""
        if len(self._listbox.curselection()) == 1:
            return self._managers[self._listbox.curselection()[0]]


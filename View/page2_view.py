import tkinter as tk


class Page2View(tk.Frame):
    """ Page 2 """

    def __init__(self, parent, submit_callback):
        """ Initialize Page 2 """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._submit_callback = submit_callback
        self._create_widgets()
        self._players = []

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """

        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self._label = tk.Label(self, text="Players")
        self._label.grid(row=1,column=0,padx=20)
        self._listbox = tk.Listbox(self,height=20,width=40)
        self._listbox.grid(row=2, column=0, padx=50)
        self._listbox.config(yscrollcommand=self._scrollbar.set)

        self._button = tk.Button(self,
                                 text="refresh",
                                 command=self._submit_callback)
        self._button.grid(row=4, column=0, padx=20)

    def get_form_data(self, players):
        """ Retrieve and save player data and insert into list"""
        self._listbox.delete(0, tk.END)
        print(players)
        for player in players:
            self._listbox.insert(tk.END, '%s %s(%s) - %s' % (player['f_name'], player['l_name'], player['id'],
                                                             player['player_position']))
        self._players = players

    def selected_item(self):
        """ return the currently selected player"""
        if len(self._listbox.curselection()) == 1:
            return self._players[self._listbox.curselection()[0]]


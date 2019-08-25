import tkinter as tk
from tkinter import messagebox as tkMessageBox


class InfoPopupView(tk.Frame):
    """ Popup Window """
    MANAGER_PAGE = 1
    PLAYER_PAGE = 2

    def __init__(self, parent, close_popup_callback, member):
        """ Initialize the Info popup view """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)
        self._member = member
        self._sample_data = ["Test12"]
        self._list_data = []
        self._close_popup_callback = close_popup_callback
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

        if self._member == None:
            self._none_widgets()
        elif self._member['type'] == 'manager':
            self._manager_widgets()
        elif self._member['type'] == 'player':
            self._player_widgets()

    def _none_widgets(self):
        """ No empety display field"""
        tk.Label(self,
                 text="No Member is selected").grid(row=0, column=0)
        tk.Button(self,
                  text="Close",
                  command=self._close_popup_callback).grid(row=1, column=0)

    def _abstract_widgets(self):
        """ Abstract Member display fields """
        tk.Label(self,
                 text="ID: %s" % self._member["id"]).grid(row=0, column=0)
        tk.Label(self,
                 text="First Name: %s" % self._member["f_name"]).grid(row=1, column=0)
        tk.Label(self,
                 text="Last Name: %s" % self._member["l_name"]).grid(row=2, column=0)
        tk.Label(self,
                 text="Address: %s" % self._member["address"]).grid(row=3, column=0)
        tk.Label(self,
                 text="Phone: %s" % self._member["phone"]).grid(row=4, column=0)
        tk.Label(self,
                 text="Type: %s" % self._member["type"]).grid(row=7, column=0)
        tk.Button(self,
                  text="Close",
                  command=self._close_popup_callback).grid(row=8, column=0)

    def _manager_widgets(self):
        """ Manager member display fields"""
        self._abstract_widgets()
        tk.Label(self,
                 text="Manager Position: %s" % self._member["manager_position"]).grid(row=5, column=0)
        tk.Label(self,
                 text="Salary: %s" % self._member["salary"]).grid(row=6, column=0)

    def _player_widgets(self):
        """ Player member display fields"""
        self._abstract_widgets()
        tk.Label(self,
                 text="Manager Position: %s" % self._member["player_position"]).grid(row=5, column=0)
        tk.Label(self,
                 text="Hourly Wage: %s" % self._member["hourly_wage"]).grid(row=6, column=0)

import tkinter as tk
from tkinter import messagebox as tkMessageBox


class DeletePopupView(tk.Frame):
    """ Delete Popup Window """
    MANAGER_PAGE = 1
    PLAYER_PAGE = 2

    def __init__(self, parent, close_popup_callback, delete_submit_callback, member):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=9, columnspan=5)
        self._close_popup_callback = close_popup_callback
        self._delete_submit_callback = delete_submit_callback
        self._member = member
        self._create_widgets()
        print(member['id'])

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        member_info = "{} {} -({}) ".format(self._member['f_name'], self._member['l_name'], self._member['id'])
        self._delete_label = tk.Label(self, text="Are you sure you want to delete %s" % member_info).grid(row=0, column=1, padx=20)
        self._yes_button = tk.Button(self,
                                     text="Yes",
                                     command=lambda :self._delete_submit_callback(self._close_current())).grid(row=2, column=0, padx=20)
        self._no_button = tk.Button(self,
                                 text="No",
                                 command=self._close_popup_callback).grid(row=2, column=2, padx=20)

    def _close_current(self):
        """ Close current popup and return member"""
        self._close_popup_callback()

        return self._member
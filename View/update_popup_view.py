import tkinter as tk
from tkinter import messagebox as tkMessageBox


class UpdatePopupView(tk.Frame):
    """ Popup for updating members Window """
    MANAGER_PAGE = 1
    PLAYER_PAGE = 2
    MANAGER_ERROR = "SALARY MUST BE A INT TYPE"
    PLAYER_ERROR = "WAGE MUST BE A FLOAT TYPE\nJERSERY MUST BE AN INT"

    def __init__(self, parent, close_popup_callback, update_submit_callback, curr_page, member):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=12, columnspan=5)
        self._close_popup_callback = close_popup_callback
        self._update_submit_callback = update_submit_callback
        self._curr_page = curr_page
        self._member = member
        self._create_widgets()

    def _none_widgets(self):
        """ Generate special widget for no selected member """

        tk.Label(self,
                 text="No Member is selected").grid(row=0, column=0)
        tk.Button(self,
                  text="Close",
                  command=self._close_popup_callback).grid(row=1, column=0)

    def _create_widgets(self):
        """ Generate Widgets depending if there is a selected member """

        if self._member == None:
            self._none_widgets()
        else:
            self._abstract_widgets()

    def _abstract_widgets(self):
        """ Generate all widgets on this.popup """

        tk.Label(self,
                 text="Update Member Id(%s)-" % (self._member["id"])).grid(row=1, column=0)
        tk.Label(self,
                 text="Name: %s %s" % (self._member["f_name"], self._member["l_name"])).grid(row=1, column=1)

        self._f_name_label = tk.Label(self, text="First Name:").grid(row=2, column=0, padx=20)
        self._f_name_entry = tk.Entry(self)
        self._f_name_entry.grid(row=2, column=1)
        self._l_name_label = tk.Label(self, text="Last Name:").grid(row=3, column=0, padx=20)
        self._l_name_entry = tk.Entry(self)
        self._l_name_entry.grid(row=3, column=1, padx=20)
        self._address_label = tk.Label(self, text="Address:").grid(row=4, column=0, padx=20)
        self._address_entry = tk.Entry(self)
        self._address_entry.grid(row=4, column=1)
        self._phone_label = tk.Label(self, text="Phone:").grid(row=5, column=0, padx=20)
        self._phone_entry = tk.Entry(self)
        self._phone_entry.grid(row=5, column=1)
        self._position_label = tk.Label(self, text="Position:").grid(row=6, column=0, padx=20)
        self._position_entry = tk.Entry(self)
        self._position_entry.grid(row=6, column=1)

        if self._curr_page == self.MANAGER_PAGE:
            self._salary_label = tk.Label(self, text="Salary:").grid(row=7, column=0, padx=20)
            self._salary_entry = tk.Entry(self)
            self._salary_entry.grid(row=7, column=1)
        elif self._curr_page == self.PLAYER_PAGE:
            self._jersey_label = tk.Label(self, text="Jersey Number:").grid(row=8, column=0, padx=20)
            self._jersey_entry = tk.Entry(self)
            self._jersey_entry.grid(row=8, column=1)
            self._wage_label = tk.Label(self, text="Hourly Wage:").grid(row=9, column=0, padx=20)
            self._wage_entry = tk.Entry(self)
            self._wage_entry.grid(row=9, column=1)

        self._button = tk.Button(self,
                                 text="Add",
                                 command=lambda:self._create_member()).grid(row=10, column=1, padx=20)

    def invalid_fields_empty(self):
        """ Checks to see if entry fields are empty and has appropriate data type"""

        empty = ""
        name_empty = self._f_name_entry.get() == empty or self._l_name_entry == empty
        personal_empty = self._address_entry.get() == empty or self._phone_entry.get() == empty
        position_empty = self._position_entry.get() == empty
        if self._curr_page == self.MANAGER_PAGE:
            try:
                abstract_empty = self._salary_entry.get() == empty or not isinstance(int(self._salary_entry.get()), int)
            except ValueError:
                print('Salary is not an int')
                return True
        else:
            try:
                abstract_empty = self._jersey_entry.get() == empty or self._wage_entry.get() == empty or not \
                                 isinstance(int(self._jersey_entry.get()), int) or not \
                                 isinstance(float(self._wage_entry.get()), float)
            except ValueError:
                print('Jersey Number is not an int or Wage is not a float')
                return True
            print(name_empty or personal_empty or position_empty or abstract_empty)
        return name_empty or personal_empty or position_empty or abstract_empty

    def _create_member(self):
        """ Create member dictionary and return after passing error checks """

        member = {}
        if self._curr_page == self.MANAGER_PAGE:
            message = self.MANAGER_ERROR
        else:
            message = self.PLAYER_ERROR

        if self.invalid_fields_empty():
            self._empty_label = tk.Label(self, text="Invalid Data field,all data fields must be filled").grid(row=11,
                                                                                                              column=0,
                                                                                                              padx=20)
            self._data_label = tk.Label(self, text=message).grid(row=11,
                                                                                                             column=1,
                                                                                                             padx=20)
        else:
            print(self._member)
            if self._curr_page == self.MANAGER_PAGE:
                member = {
                    "id": self._member['id'],
                    "f_name": self._f_name_entry.get(),
                    "l_name": self._l_name_entry.get(),
                    "address": self._address_entry.get(),
                    "phone": self._phone_entry.get(),
                    "position": self._position_entry.get(),
                    "salary": int(self._salary_entry.get()),
                    "type": "manager",
                    "jersey_number": 0,
                    "wage": 0
                }
            elif self._curr_page == self.PLAYER_PAGE:
                member = {
                    "id": self._member['id'],
                    "f_name": self._f_name_entry.get(),
                    "l_name": self._l_name_entry.get(),
                    "address": self._address_entry.get(),
                    "phone": self._phone_entry.get(),
                    "position": self._position_entry.get(),
                    "salary": 0,
                    "type": "player",
                    "jersey_number": int(self._jersey_entry.get()),
                    "wage": float(self._wage_entry.get())
                }
            self._update_submit_callback(member)
            self._close_popup_callback()

        return member

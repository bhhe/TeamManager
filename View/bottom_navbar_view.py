import tkinter as tk


class BottomNavbarView(tk.Frame):
    """ Bottom Navigation Bar """

    def __init__(self, parent, delete_popup_callback, add_page_popup_callback, update_page_popup_callback,
                 info_page_popup_callback):
        """ Initialize the bottom nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._delete_popup_callback = delete_popup_callback
        self._add_page_popup_callback = add_page_popup_callback
        self._update_page_popup_callback = update_page_popup_callback
        self._info_page_popup_callback = info_page_popup_callback
        self._create_widgets()


    def _create_widgets(self):
        """ Nav bar widgets for add,info,delete and update"""
        self._add_btn = tk.Button(self,
                           text="Add",
                           fg="red",
                           command=self._add_page_popup_callback)

        self._update_btn = tk.Button(self,
                           text="Update",
                           fg="red",
                           command=self._update_page_popup_callback)
        self._delete_btn = tk.Button(self,
                           text="Delete",
                           fg="red",
                           command=self._delete_popup_callback)
        self._info_btn = tk.Button(self,
                           text="Info",
                           fg="red",
                           command=self._info_page_popup_callback)

        self._add_btn.grid(row=0,column=1,padx=20)
        self._update_btn.grid(row=0,column=2,padx=20)
        self._delete_btn.grid(row=0,column=3,padx=20)
        self._info_btn.grid(row=0,column=4,padx=20)

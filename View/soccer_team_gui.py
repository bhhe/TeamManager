import tkinter as tk
from tkinter import messagebox
import requests
from View.top_navbar_view import TopNavbarView
from page1_view import Page1View
from page2_view import Page2View
from bottom_navbar_view import BottomNavbarView
from popup_view import PopupView
from delete_popup_view import DeletePopupView
from update_popup_view import UpdatePopupView
from add_popup_view import AddPopupView
from info_popup_view import InfoPopupView
from Model.manager import Manager
from Model.player import Player


class MainAppController(tk.Frame):
    """ Main Application for GUI """
    MANAGER_PAGE = 1
    PLAYER_PAGE = 2

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._page_callback, self._page_popup_callback)
        self._data = self._get_endpoints('Player')
        self._page1 = Page1View(self, self._page1_submit_callback)
        self._page2 = Page2View(self, self._page2_submit_callback)
        self._bottom_navbar = BottomNavbarView(self, self._delete_page_popup_callback, self._add_page_popup_callback,
                                               self._update_page_popup_callback, self._info_page_popup_callback)
        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._page1.grid(row=1, columnspan=4, pady=10)

        self._curr_page = TopNavbarView.PAGE1
        # Hide Page 2 by default
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)
        self._page1_submit_callback()
        self._page2_submit_callback()

    def _page_callback(self):
        """ Handle Switching Between Pages """

        curr_page = self._top_navbar.curr_page.get()
        if (self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE1):
            self._page1.grid_forget()
            self._page2.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE2
            self._page2_submit_callback()
        elif (self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE2):
            self._page2.grid_forget()
            self._page1.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE1
            self._page1_submit_callback()

    def _page_popup_callback(self):
        """ Page popup call back for testing """
        self._popup_win = tk.Toplevel()
        self._popup = PopupView(self._popup_win, self._close_popup_callback)

    def _add_page_popup_callback(self):
        """ Add_page_popup callback """
        self._popup_win = tk.Toplevel()
        self._popup = AddPopupView(self._popup_win, self._close_popup_callback, self._add_submit_callback,
                                   self._curr_page)

    def _update_page_popup_callback(self):
        """ Update_page_popup callback """
        self._popup_win = tk.Toplevel()
        item = 0

        if self._curr_page == self.MANAGER_PAGE:
            item = self._page1.selected_item()
        elif self._curr_page == self.PLAYER_PAGE:
            item = self._page2.selected_item()
        self._popup = UpdatePopupView(self._popup_win, self._close_popup_callback, self._update_submit_callback,
                                          self._curr_page, item)

    def _info_page_popup_callback(self):
        """ Info_page_popup callback"""
        self._popup_win = tk.Toplevel()
        item = 0

        if self._curr_page == self.MANAGER_PAGE:
            item = self._page1.selected_item()
        elif self._curr_page == self.PLAYER_PAGE:
            item = self._page2.selected_item()
        self._popup = InfoPopupView(self._popup_win, self._close_popup_callback, item)

    def _delete_page_popup_callback(self):
        """ Delete_popup calback"""
        self._popup_win = tk.Toplevel()
        item = 0

        if self._curr_page == self.MANAGER_PAGE:
            item = self._page1.selected_item()
        elif self._curr_page == self.PLAYER_PAGE:
            item = self._page2.selected_item()

        self._popup = DeletePopupView(self._popup_win, self._close_popup_callback, self._delete_submit_callback,
                                      item)

    def _close_popup_callback(self):
        """ close call back"""
        self._popup_win.destroy()

    def _page1_submit_callback(self):
        """ Manager page call back """
        self._page1.get_form_data(self._get_endpoints('manager'))
        return self._get_endpoints('manager')

    def _page2_submit_callback(self):
        """ Player page call back"""
        self._page2.get_form_data(self._get_endpoints('player'))
        return self._get_endpoints('player')

    def _add_submit_callback(self, member):
        """ add member submit callback """
        status_code = self._add_member(member)
        if self._curr_page == self.MANAGER_PAGE:
            self._page1_submit_callback()
        elif self._curr_page == self.PLAYER_PAGE:
            self._page2_submit_callback()

        return status_code

    def _delete_submit_callback(self, member):
        """ Delete member submit callback"""
        status_code = self._delete_member(member['id'])
        if self._curr_page == self.MANAGER_PAGE:
            self._page1_submit_callback()
        elif self._curr_page == self.PLAYER_PAGE:
            self._page2_submit_callback()

        return status_code

    def _update_submit_callback(self, member):
        """ Update member subtmit callback """
        status_code = self._update_member(member)
        if self._curr_page == self.MANAGER_PAGE:
            self._page1_submit_callback()
        elif self._curr_page == self.PLAYER_PAGE:
            self._page2_submit_callback()

        return status_code

    def _get_endpoints(self, type):
        """ Get by type request """
        response = requests.get('http://127.0.0.1:5000/soccer_team/member/all/%s' % type)
        if response.status_code == 200:
            return response.json()

    def _get_info(self, id):
        """ Get member request"""
        response = requests.get('http://127.0.0.1:5000/soccer_team/member/%s' %id)
        if response.status_code == 200:
            return response.json()

    def _delete_member(self, id):
        """ Delete member request"""
        if id != None:
            response = requests.delete('http://127.0.0.1:5000/soccer_team/member/%s' % id)
            if response.status_code != 200:
                return response
            self._message_popup("delete", response.status_code)

    def _add_member(self, member):
        """ Add member request"""
        response = requests.post('http://127.0.0.1:5000/soccer_team/member', json=member)
        if response.status_code != 200:
            return response
        self._message_popup("add", response.status_code)

    def _update_member(self, member):
        """ Update member request"""
        response = requests.put('http://127.0.0.1:5000/soccer_team/member/%s' % str(member['id']), json=member)
        if response.status_code == 200:
            return response
        self._message_popup("update", response.status_code)

    def _quit_callback(self):
        """ quit """
        self.quit()

    def _message_popup(self, message, status_code):
        """ Response code checking and messagebox display"""
        if status_code == 200:
            messagebox.showinfo("Message", "Successful %s" % message)
        else:
            messagebox.showinfo("Message", "Failed %s" % message)


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()


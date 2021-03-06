import random

from tkinter import Tk

from tkouter import *
from tkouter import settings



class RandomSelector(TkOutWidget):

    # layout
    layout = 'randsel.html'

    # model
    item = StringField(default='Item Name')
    hide = BoolField(default=False)

    def __init__(self, master):
        super().__init__(master)
        self._items = []

    def sel(self):
        if self._items:
            self.item = random.choice(self._items)

    def add(self):
        self._items.append(self.item)
        self.listbox.insert('end', self.item)

    def show(self):
        if self.hide:
            self.itemframe.pack_forget()
        else:
            self.itemframe.pack(fill="both", expand="1")

    def quit(self):
        self.master.destroy()


if __name__ == '__main__':
    root = Tk()
    rs = RandomSelector(root)
    rs.pack()
    root.mainloop()
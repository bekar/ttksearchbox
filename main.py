#!/usr/bin/python3

# Translated from Tcl code by Schelte Bron, http://wiki.tcl.tk/18188

try:
    from tkinter import *
    from tkinter import ttk
except:
    from Tkinter import *
    import ttk

import os
filepath=os.path.abspath(__file__)
fullpath=os.path.dirname(filepath)

def entrystyle():
    data = open(fullpath+"/pic.dat").read()
    global s1, s2
    s1 = PhotoImage("search1", data=data, format="gif -index 0")
    s2 = PhotoImage("search2", data=data, format="gif -index 1")
    style = ttk.Style()
    style.element_create("Search.field", "image", "search1",
        ("focus", "search2"), border=[22, 7, 14], sticky="ew")
    style.layout("Search.entry", [
        ("Search.field", {"sticky": "nswe", "border": 1, "children":
            [("Entry.padding", {"sticky": "nswe", "children":
                [("Entry.textarea", {"sticky": "nswe"})]
            })]
        })]
    )
    style.configure("Search.entry", background="#b2b2b2")

if __name__ == '__main__':
    root = Tk()
    root.config(background="#b2b2b2")
    entrystyle()
    ttk.Entry(root, style="Search.entry", width=20).pack(expand=NO)

    root.bind("<Key-Escape>", lambda event: quit())
    root.mainloop()

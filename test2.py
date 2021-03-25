import tkinter as tk
from tkinter import ttk

root = tk.Tk()

notebook = ttk.Notebook(root)
notebook.pack()

frame1 = tk.Frame(notebook, bg='red', width=400, height=400)
frame1.pack_propagate(False)

frame2 = tk.Frame(notebook, bg='blue', width=400, height=400)
frame2.pack_propagate(False)

notebook.add(frame1, text='frame 1')
notebook.add(frame2, text='frame 2')

var = tk.StringVar(root, 'a b c d e f g')
listbox = tk.Listbox(notebook, listvariable=var)

def display_listbox(event):
    tab = notebook.tabs()[notebook.index('current')]
    listbox.pack(in_=tab)

notebook.bind('<<NotebookTabChanged>>', display_listbox)

root.mainloop()
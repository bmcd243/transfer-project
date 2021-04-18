# import tkinter modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkcalendar import *
from tkmacosx import Button

root = Tk()

available_seats = [[False, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]]

for i in range(10):
    letter = chr(i+97).upper()
    row_label = Label(root, text=letter)
    row_label.grid(row=i+1, column=0)
    for j in range(20):
        column_label = Label(root, text=j+1)
        column_label.grid(row=0, column=j+1)
        # linear search through each position in the 2D list
        if available_seats[i][j] == True:
            button_colour = "green"
        else:
            button_colour = "red"
        b = Button(root, bg=button_colour, height=20, width=50)
        b.grid(row=i + 1, column=j+1)


# for j in range(20):
#     for k in range(20):
#         if available_seats_1[k] == True:
#             button_colour = "green"
#         b = Button(root, bg=button_colour, height=20, width=50)
#         b.grid(row=1, column=j)

root.mainloop()
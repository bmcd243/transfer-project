# import tkinter modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkcalendar import *
from tkmacosx import Button

root = Tk()

booked_seat = "B2"

available_seats = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]

available_seats_1 = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

# for i in range(10):
#     for j in range(20):
#         print(i)
#         for k in range(10):
#             if available_seats[i][k] == True:
#                 button_colour = "red"
#         b = Button(root, bg=button_colour, height=2, width=5)
#         b.grid(row=i + 1, column=j)


for j in range(20):
    for k in range(20):
        if available_seats_1[k] == True:
            button_colour = "green"
        b = Button(root, bg=button_colour, height=20, width=50)
        b.grid(row=1, column=j)

root.mainloop()
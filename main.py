# import tkinter modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
# from PIL import ImageTk, Image
from tkcalendar import *

# import modules for restart functionality
import os
import sys
import time

# import sqlite 3 for database functionality
import sqlite3

# import datetime module
import datetime

# fetching dates
current_date = datetime.datetime.now()
current_today = current_date.strftime("%w")
current_month = current_date.strftime("%m")
current_year = current_date.strftime("%Y")
full_date = datetime.date.today()


def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)


# define self
class tkinterApp(Tk):

	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		# creating a container
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		# initialising frames to an empty array
		self.frames = {}

		for F in (welcome_frame, new_booking_frame, seat_selection_frame):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame("welcome_frame")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

class welcome_frame(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		label = Label(self, text="This is the start page")
		label.pack(side="top", fill="x", pady=10)

		button1 = Button(self, text="Go to new booking frame",
							command=lambda: controller.show_frame("new_booking_frame"))
		button2 = Button(self, text="Go to seat selection frame",
							command=lambda: controller.show_frame("seat_selection_frame"))
		button1.pack()
		button2.pack()

class new_booking_frame(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		label = Label(self, text="This is page 1")
		label.pack(side="top", fill="x", pady=10)
		button = Button(self, text="Go to the start page",
						   command=lambda: controller.show_frame("welcome_frame"))
		button.pack()


class seat_selection_frame(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		label = Label(self, text="This is page 2")
		label.pack(side="top", fill="x", pady=10)
		button = Button(self, text="Go to the start page",
						   command=lambda: controller.show_frame("welcome_frame"))
		button.pack()


if __name__ == "__main__":
	app = tkinterApp()
	app.geometry("1000x800")
	app.title("Collyer's Booking System")
	app.mainloop()

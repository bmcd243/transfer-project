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


def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)

def create_database():

	connection = sqlite3.connect('collyers_booking_system.db')

	cursor = connection.cursor()

	customer_table = """CREATE TABLE IF NOT EXISTS
	customer(
	customer_id INTEGER PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	phone_number TEXT,
	)"""

	booking_table = """CREATE TABLE IF NOT EXISTS
		booking(
		booking_id INTEGER PRIMARY KEY,
		customer_id INTEGER,
		night INTEGER,
		cost REAL,
		FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
		)"""

	performance_table = """CREATE TABLE IF NOT EXISTS
		performance(
		performance_id INTEGER PRIMARY KEY,
		seat_id INTEGER,
		booking_id INTEGER,
		FOREIGN KEY (seat_id) REFERENCES seat(seat_id)
		FOREIGN KEY (booking_id) REFERENCES booking(booking_id)
		)"""

	seat_table = """CREATE TABLE IF NOT EXISTS
	seat(
		seat_id INTEGER PRIMARY KEY,
		type_of_seat TEXT,
	)"""




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

		for F in (welcome_frame, new_booking_frame, edit_booking_frame):
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
		label = Label(self, text="Hello and welcome to the Booking System - please select one of the buttons below.")
		label.pack(side="top", fill="x", pady=10)

		button1 = Button(self, text="Create new booking",
							command=lambda: controller.show_frame("new_booking_frame"))
		button2 = Button(self, text="Edit existing booking",
							command=lambda: controller.show_frame("edit_booking_frame"))
		button1.pack()
		button2.pack()

class new_booking_frame(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		label = Label(self, text="NEW BOOKING")
		label.grid(row=1, column=1, pady=10)
		button = Button(self, text="HOME PAGE",
						   command=lambda: controller.show_frame("welcome_frame"))
		button.grid(row=0, column=0, pady=10)


class edit_booking_frame(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		label = Label(self, text="🚧 PAGE IN PROGRESS 🚧")
		label.grid(row=1, column=1, pady=10)
		button = Button(self, text="HOME PAGE",
						   command=lambda: controller.show_frame("welcome_frame"))
		button.grid(row=0, column=0)

		print("please work")


if __name__ == "__main__":
	app = tkinterApp()
	app.geometry("1000x800")
	app.title("Collyer's Booking System")
	app.mainloop()

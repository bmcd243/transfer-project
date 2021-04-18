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

root = Tk()

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
	phone_number INTEGER,
	type_of_customer TEXT
	)"""

	booking_table = """CREATE TABLE IF NOT EXISTS
		booking(
		booking_id TEXT PRIMARY KEY,
		customer_id INTEGER,
		night INTEGER,
		cost REAL,
		FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
		)"""

	performance_table = """CREATE TABLE IF NOT EXISTS
		performance(
		performance_id TEXT PRIMARY KEY,
		seat_id TEXT,
		booking_id INTEGER,
		FOREIGN KEY (seat_id) REFERENCES seat(seat_id)
		FOREIGN KEY (booking_id) REFERENCES booking(booking_id)
		)"""

	seat_table = """CREATE TABLE IF NOT EXISTS
	seat(
		seat_id TEXT PRIMARY KEY,
		type_of_seat TEXT
	)"""

	cursor.execute(customer_table)
	cursor.execute(booking_table)
	cursor.execute(performance_table)
	cursor.execute(seat_table)

	customer_default_values = [
		(1, 'Steve', 'Smith', '07748214857', 'Reduced'),
		(2, 'Sarah', 'McDonald', '07543997564', 'Reduced'),
		(3, 'Will', 'Stevenson', '07734294756', 'Normal'),
		(4, 'Steve', 'Swimswam', '07654384998', 'Normal'),
		(5, 'Harry', 'Reeto', '07754834768', 'Normal')
	]

	cursor.executemany("INSERT INTO customer (customer_id, first_name, last_name, phone_number, type_of_customer) VALUES (?, ?, ?, ?, ?)", customer_default_values)
	connection.commit()

	booking_default_values = [
		('1-1', 1, 1, 5.00),
		('2-2', 2, 2, 5.00),
		('1-3', 3, 1, 10.00),
		('3-4', 4, 3, 10.00),
		('2-5', 5, 2, 10.00)
	]

	cursor.executemany("INSERT INTO booking (booking_id, customer_id, night, cost) VALUES (?, ?, ?, ?)", booking_default_values)
	connection.commit()

	performance_default_values = [
		('1-1-B18', 'B18', '1-1'),
		('2-2-C20', 'C20', '2-2'),
		('1-3-D12', 'D12', '1-3'),
		('3-4-E13', 'E13', '3-4'),
		('2-5-E02', 'E02', '2-5')
	]

	cursor.executemany("INSERT INTO performance (performance_id, seat_id, booking_id) VALUES (?, ?, ?)", performance_default_values)
	connection.commit()

	seat_default_values = [
		('B18', 'Regular'),
		('C20', 'Regular'),
		('D12', 'Special'),
		('E13', 'Regular'),
		('E02', 'Regular')
	]

	cursor.executemany("INSERT INTO seat (seat_id, type_of_seat) VALUES (?, ?)", seat_default_values)
	connection.commit()

def start():
	raise_frame(welcome_frame, welcome_frame)

def welcome():
	Button(welcome_frame, text='Start new booking', command=lambda:raise_frame(welcome_frame, choose_night_frame)).grid(row=1, column=3)
	Label(welcome_frame, text='Welcome to the Collyers Booking System, please select one of the buttons below.').grid(row=0, column=3)

	def fetch_current_dates():
			connection = sqlite3.connect('collyers_booking_system.db')
			cursor = connection.cursor()

			first_night = cursor.execute("""SELECT*(booking_id) FROM booking WHERE night=1""")
			print(first_night)

	Label(welcome_frame, text='Current availability').grid(row=2, column=3)

def choose_night():
	Label(choose_night_frame, text="We are now on the second frame").pack()
	Button(choose_night_frame, text='Back', command=lambda:raise_frame(choose_night_frame, welcome_frame)).pack()

def seat_selection():
	print("")

def enter_details():
	print("")

def confirmation():
	print("")

def receipt():
	print("")

def raise_frame(current_frame, frame):
	for widget in current_frame.winfo_children():
		widget.destroy()
	frame.tkraise()
	if frame == welcome_frame:
		welcome()
	elif frame == choose_night_frame:
		choose_night()
	elif frame == seat_selection_frame:
		seat_selection()
	elif frame == enter_details_frame:
		enter_details()
	elif frame == confirmation_frame:
		confirmation()
	elif frame == receipt_frame:
		receipt()



welcome_frame = Frame(root)
choose_night_frame = Frame(root)
seat_selection_frame = Frame(root)
enter_details_frame = Frame(root)
confirmation_frame = Frame(root)
receipt_frame = Frame(root)


for frame in (welcome_frame, choose_night_frame, seat_selection_frame, enter_details_frame, confirmation_frame, receipt_frame):
	frame.grid(row=0, column=0, sticky='news')

start()
create_database()


root.geometry("1000x800")
root.title("Collyer's Booking System")
root.mainloop()

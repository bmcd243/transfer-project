# import tkinter modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
# from PIL import ImageTk, Image
from tkcalendar import *
from tkinter import messagebox


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
		FOREIGN KEY (seat_id) REFERENCES seat(seat_id),
		FOREIGN KEY (booking_id) REFERENCES booking(booking_id),
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
	global first_night_availability
	global second_night_availability
	global third_night_availability

	Button(welcome_frame, text='Start new booking', command=lambda:raise_frame(welcome_frame, choose_night_frame)).grid(row=1, column=3, pady=10, padx=10)
	Label(welcome_frame, text='Welcome to the Collyers Booking System, please select one of the buttons below.').grid(row=0, column=3, pady=10, padx=10)

	def fetch_current_dates():
		global first_night_availability
		global second_night_availability
		global third_night_availability

		connection = sqlite3.connect('collyers_booking_system.db')
		cursor = connection.cursor()

		# FIRST NIGHT

		cursor.execute("""SELECT * FROM booking WHERE night=1""")
		first_night = cursor.fetchall()

		i=0
		for row in first_night:
			i = i + 1		
		first_night_availability = 200-i

		# SECOND NIGHT

		cursor.execute("""SELECT * FROM booking WHERE night=2""")
		second_night = cursor.fetchall()

		j=0
		for row in second_night:
			j = j + 1		
		second_night_availability = 200-j

		# THIRD NIGHT

		cursor.execute("""SELECT * FROM booking WHERE night=3""")
		third_night = cursor.fetchall()

		k=0
		for row in third_night:
			k=k+1
		
		third_night_availability = 200-k


		Label(welcome_frame, text='First night	-->	' + str(first_night_availability) + ' seats avaiable').grid(row=3, column=3, pady=10, padx=10)
		Label(welcome_frame, text='Second night	-->	' + str(second_night_availability) + ' seats avaiable').grid(row=4, column=3, pady=10, padx=10)				
		Label(welcome_frame, text='Third night	-->	' + str(third_night_availability) + ' seats avaiable').grid(row=5, column=3, pady=10, padx=10)				
			
	
	fetch_current_dates()

	Label(welcome_frame, text='⬇️CURRENT AVAILABILITY⬇️').grid(row=2, column=3, pady=10, padx=10)

def choose_night():
	Label(choose_night_frame, text="NEW BOOKING").grid(column=3, row=0, pady=10, padx=10)
	Button(choose_night_frame, text='Back', command=lambda:raise_frame(choose_night_frame, welcome_frame)).grid(row=0, column=0)

	Label(choose_night_frame, text="⬇️Select a night below⬇️").grid(column=3, row=1, pady=10, padx=10)

	night_options = [
		"Night one",
		"Night two",
		"Night three"
	]

	variable = StringVar(choose_night_frame)
	variable.set(night_options[0])

	night_dropdown = OptionMenu(choose_night_frame, variable, *night_options)
	night_dropdown.grid(row=2, column=3, pady=10, padx=10)

	def confirm_availability():
		chosen_night = variable.get()

		if chosen_night == "Night one":
			if first_night_availability < 1:
				messagebox.showerror(title='Night fully booked', message='This night is fully booked, please select a different night')
			else:
				seat_selection(chosen_night)

		if chosen_night == "Night two":
			if second_night_availability < 1:
				messagebox.showerror(title='Night fully booked', message='This night is fully booked, please select a different night')
			else:
				seat_selection(chosen_night)

		if chosen_night == "Night three":
			if third_night_availability < 1:
				messagebox.showerror(title='Night fully booked', message='This night is fully booked, please select a different night')
			else:
				seat_selection(chosen_night)


	Button(choose_night_frame, text="CONFIRM NIGHT", command=lambda: confirm_availability()).grid(column=3, row=3, pady=10, padx=10)

def seat_selection(chosen_night):

	def check_seat_availability(chosen_night):
		if chosen_night == "Night one":
			night_number = 1
		if chosen_night == "Night two":
			night_number = 2
		if chosen_night == "Night three":
			night_number = 3

		connection = sqlite3.connect('collyers_booking_system.db')
		cursor = connection.cursor()

		cursor.execute("""SELECT seat_id FROM performance INNER JOIN booking ON night=?""", (night_number))
		booked_seats = cursor.fetchall()

		print(booked_seats)
		

	check_seat_availability(chosen_night)


	# for i in range(10):
    # letter = chr(i+97).upper()
    # row_label = Label(root, text=letter)
    # row_label.grid(row=i+1, column=0)
    # for j in range(20):
    #     column_label = Label(root, text=j+1)
    #     column_label.grid(row=0, column=j+1)
    #     # linear search through each position in the 2D list
    #     if available_seats[i][j] == True:
    #         button_colour = "green"
    #     else:
    #         button_colour = "red"
    #     b = Button(root, bg=button_colour, height=20, width=50)
    #     b.grid(row=i + 1, column=j+1)

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
# create_database()


root.geometry("1000x800")
root.title("Collyer's Booking System")
root.mainloop()

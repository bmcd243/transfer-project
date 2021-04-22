# import tkinter modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
# from PIL import ImageTk, Image
from tkcalendar import *
from tkinter import messagebox
from tkmacosx import Button


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
	customer_id INTEGER AUTO_INCREMENT,
	first_name TEXT,
	last_name TEXT,
	phone_number INTEGER,
	type_of_customer TEXT,
	PRIMARY KEY(customer_id)
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
	global chosen_night

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
		global chosen_night

		chosen_night = variable.get()

		if chosen_night == "Night one":
			if first_night_availability < 1:
				messagebox.showerror(title='Night fully booked', message='This night is fully booked, please select a different night')
			else:
				raise_frame(choose_night_frame, seat_selection_frame)

		if chosen_night == "Night two":
			if second_night_availability < 1:
				messagebox.showerror(title='Night fully booked', message='This night is fully booked, please select a different night')
			else:
				raise_frame(choose_night_frame, seat_selection_frame)

		if chosen_night == "Night three":
			if third_night_availability < 1:
				messagebox.showerror(title='Night fully booked', message='This night is fully booked, please select a different night')
			else:
				raise_frame(choose_night_frame, seat_selection_frame)


	Button(choose_night_frame, text="CONFIRM NIGHT", command=lambda: confirm_availability()).grid(column=3, row=3, pady=10, padx=10)

def seat_selection():

	def check_selected_seat(selected_seat, available_seats):
		print(selected_seat)

		boo = False

		for i in range(10):
			for j in range(20):
				if selected_seat == available_seats[i][j]:
					boo = True
					raise_frame(seat_selection_frame, enter_details_frame)
		
		if boo == False:
			messagebox.showerror(title='Seat not available', message='This seat is booked for this night, please choose a different seat.')

		


	def display_seats(available_seats):
		# for each row
		for i in range(10):
			letter = chr(i+97).upper()
			row_label = Label(seat_selection_frame, text=letter)
			row_label.grid(row=i+1, column=0)
			# for each column
			for j in range(20):
				column_label = Label(seat_selection_frame, text=j+1)
				column_label.grid(row=0, column=j+1)

				# linear search through each position in the 2D list
				if available_seats[i][j] == 'False':
					button_colour = "red"
				else:
					button_colour = "green"

				print (button_colour)

				b = Button(seat_selection_frame, bg=button_colour, height=20, width=50)
				b.grid(row=i + 1, column=j+1)



		Label(seat_selection_frame, text='Enter seat -->').grid(row=13, column=0, padx=5, pady=20, columnspan=10, sticky=W)

		seat_choose_field = Entry(seat_selection_frame)
		seat_choose_field.grid(row=13, column=1, padx=5, pady=20, columnspan=10)

		def fetch_entry():
			selected_seat = seat_choose_field.get()

			check_selected_seat(selected_seat, available_seats)

		seat_select = Button(seat_selection_frame, text="Choose seat", command=lambda: fetch_entry())
		seat_select.grid(row=14, column=0, padx=5, pady=20, columnspan=10)

	def check_seat_availability(chosen_night):
		if chosen_night == "Night one":
			night_number = 1
		if chosen_night == "Night two":
			night_number = 2
		if chosen_night == "Night three":
			night_number = 3

		connection = sqlite3.connect('collyers_booking_system.db')
		cursor = connection.cursor()

		# cursor.execute("""SELECT seat_id FROM performance WHERE booking_id IN (SELECT * FROM booking WHERE night = ?)""", (night_number,))

		sql = """
		SELECT p.seat_id 
		FROM performance p INNER JOIN booking b 
		ON b.booking_id = p. booking_id
		WHERE b.night=?
		"""
		cursor.execute(sql, (night_number,))

		booked_seats = cursor.fetchall()

		# array for all seats

		available_seats = [['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18', 'I19', 'I20'], ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20'] ]

		print(booked_seats)

		length = len(booked_seats)
		print(length)

		str1 = ""

		for k in range(length):
			as_string = str1.join(booked_seats[k])
			print(as_string)
			for i in range(10):
				for j in range(20):
					if available_seats[i][j] == as_string:
						available_seats[i][j] = 'False'

		print(available_seats)

		# display seat selection
		display_seats(available_seats)

	check_seat_availability(chosen_night)



def enter_details():

	Label(enter_details_frame, text='Enter details below').grid(row=0, column=0, padx=5, pady=20)

	Label(enter_details_frame, text='Enter first name -->').grid(row=1, column=0, padx=5, pady=20)

	enter_first_name = Entry(enter_details_frame)
	enter_first_name.grid(row=1, column=1, padx=5, pady=20)

	Label(enter_details_frame, text='Enter last name -->').grid(row=2, column=0, padx=5, pady=20)

	enter_last_name = Entry(enter_details_frame)
	enter_last_name.grid(row=2, column=1, padx=5, pady=20)

	Label(enter_details_frame, text='Enter phone number -->').grid(row=3, column=0, padx=5, pady=20)

	enter_phone_number = Entry(enter_details_frame)
	enter_phone_number.grid(row=3, column=1, padx=5, pady=20)

	dropdown_type_of_customer

	def add_details_to_database(first_name, last_name, phone_number, type_of_customer):
		
		connection = sqlite3.connect('collyers_booking_system.db')
		cursor = connection.cursor()

		cursor.executemany("INSERT INTO customer (first_name, last_name, phone_number, type_of_customer) VALUES (?, ?, ?, ?)", first_name, last_name, phone_number, type_of_customer)
		connection.commit()


	def fetch_details():
		first_name = enter_first_name.get()
		last_name = enter_last_name.get()
		phone_number = enter_phone_number.get()

		customer_options = [
			"Standard (Adult - £10)"
			"Reduced (Under 18, Concession - £5"
		]

		variable = StringVar(enter_details_frame)
		variable.set(customer_options[0])

		type_of_customer_dropdown = OptionMenu(enter_details_frame, variable, *customer_options)


		add_details_to_database(first_name, last_name, phone_number)



	Button(enter_details_frame, text='Confirm details', command=lambda: fetch_details())

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

from tkinter import *
from tkinter import ttk

root = Tk()


def start():
	raise_frame(welcome_frame, welcome_frame)

def welcome():
	Button(welcome_frame, text='New booking', command=lambda:raise_frame(welcome_frame, choose_night_frame)).pack()
	Label(welcome_frame, text='FRAME 1').pack()

def choose_night():
	Button(choose_night_frame, text='Back', command=lambda:raise_frame(choose_night_frame, welcome_frame)).pack()
	Label(choose_night_frame, text='FRAME 2').pack()

def raise_frame(current_frame, frame):
	current_frame.destroy()
	frame.tkraise()
	if frame == welcome_frame:
		welcome()
	elif frame == choose_night_frame:
		choose_night()

welcome_frame = Frame(root)
choose_night_frame = Frame(root)


for frame in (welcome_frame, choose_night_frame):
	frame.grid(row=0, column=0, sticky='news')

start()

root.mainloop()
# import tkinter modules
from tkinter import *
from tkinter import ttk

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

		for F in (welcome_frame, edit_booking_frame):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame("welcome_frame")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()
		frame.event_generate("<<ShowFrame>>")

class welcome_frame(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller


class edit_booking_frame(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.bind("<<ShowFrame>>", self.on_show_frame)

		def on_show_frame(self, event):
			print("I am being shown...")



if __name__ == "__main__":
	app = tkinterApp()
	app.geometry("1000x800")
	app.mainloop()

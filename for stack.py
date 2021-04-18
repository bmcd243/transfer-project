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

		self.frames['welcome_frame'] = welcome_frame(parent=controller, controller=self)
		self.frames['edit_booking_frame'] = edit_booking_frame(parent=controller, controller=self)

		frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame("welcome_frame")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

class welcome_frame(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		button2 = Button(self,  command=lambda: controller.show_frame("edit_booking_frame"))
		button2.pack()


class edit_booking_frame(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		print("hello")


if __name__ == "__main__":
	app = tkinterApp()
	app.geometry("1000x800")
	app.mainloop()

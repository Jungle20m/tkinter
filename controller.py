


import tkinter as tk

from second_view import Screen





class Controller():
	def __init__(self, master):
		# View
		self.view = Screen(master) 
		# Model
		# self.model = Model()


if __name__ == '__main__':
	master = tk.Tk()
	controller = Controller(master)
	master.mainloop()
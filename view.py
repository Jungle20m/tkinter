import cv2

import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox


class Screen():
	
	def __init__(self, master):
		self.master = master
		self.create_ui()

	def create_ui(self):
		frame1 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		frame2 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		frame3 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		frame4 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		frame5 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		frame6 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		frame7 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		 
		frame1.grid(column=0, row=0, sticky="nsew")
		frame2.grid(column=0, row=1, sticky="nsew")
		frame3.grid(column=1, row=0, sticky="nsew")
		frame4.grid(column=1, row=1, sticky="nsew")
		frame5.grid(column=2, row=0, sticky="nsew")
		frame6.grid(column=2, row=1, sticky="nsew")
		frame7.grid(column=3, row=0, sticky="nsew", rowspan=2)

		# Image
		self.image1 = self.create_image_label(frame1, 300, 300)
		self.image2 = self.create_image_label(frame2, 300, 300)
		self.image3 = self.create_image_label(frame3, 300, 300)
		self.image4 = self.create_image_label(frame4, 300, 300)
		self.image5 = self.create_image_label(frame5, 300, 300)
		self.image6 = self.create_image_label(frame6, 300, 300)

		self.image1.pack(fill=tk.BOTH, expand=tk.YES)
		self.image2.pack(fill=tk.BOTH, expand=tk.YES)
		self.image3.pack(fill=tk.BOTH, expand=tk.YES)
		self.image4.pack(fill=tk.BOTH, expand=tk.YES)
		self.image5.pack(fill=tk.BOTH, expand=tk.YES)
		self.image6.pack(fill=tk.BOTH, expand=tk.YES)

		# Information
		label_name = self.create_infor_label(frame7, "Họ tên:")
		label_position = self.create_infor_label(frame7, "Vị trí:")
		label_plate_number = self.create_infor_label(frame7, "Biển số xe:")
		label_timein = self.create_infor_label(frame7, "Thời gian vào:")
		label_timeout = self.create_infor_label(frame7, "Thời gian ra:")

		self.name = self.create_infor_label(frame7, "Nguyễn Văn Đức", font=("Helvetica", 16, 'bold'), width=20)
		self.position = self.create_infor_label(frame7, "DEV", font=("Helvetica", 16, 'bold'), width=20)
		self.plate_number = self.create_infor_label(frame7, "03829", font=("Helvetica", 16, 'bold'), width=20)
		self.timein = self.create_infor_label(frame7, "07:13:21", font=("Helvetica", 16, 'bold'), width=20)
		self.timeout = self.create_infor_label(frame7, "18:06:03", font=("Helvetica", 16, 'bold'), width=20)

		label_name.grid(row=0, column=0, pady=10, padx=20, sticky=tk.W)
		label_position.grid(row=1, column=0, pady=10, padx=20, sticky=tk.W)
		label_plate_number.grid(row=2, column=0, pady=10, padx=20, sticky=tk.W)
		label_timein.grid(row=3, column=0, pady=10, padx=20, sticky=tk.W)
		label_timeout.grid(row=4, column=0, pady=10, padx=20, sticky=tk.W)
		self.name.grid(row=0, column=1, sticky=tk.W)
		self.position.grid(row=1, column=1, sticky=tk.W)
		self.plate_number.grid(row=2, column=1, sticky=tk.W)
		self.timein.grid(row=3, column=1, sticky=tk.W)
		self.timeout.grid(row=4, column=1, sticky=tk.W)

		button = tk.Button(frame7, text="hello", width=20, command=self.show_error)
		button.grid(row=5, columnspan=2, pady=80)
		
	def create_image_label(self, container, width, height, background='#e8e8e8'):
		# default no_image path
		default_image_path = 'image/no_image.png' 
		image = cv2.imread(default_image_path)
		image = cv2.resize(image, (width, height))
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = Image.fromarray(image)
		image = ImageTk.PhotoImage(image)
		label = tk.Label(container, image=image, width=width, height=height, background=background)
		# keep reference for display image
		label.image = image 
		return label

	def create_infor_label(self, container, text, font=("Helvetica", 16), fg="#282828", width=15):
		label = tk.Label(container, text=text, font=font, fg=fg, width=width, anchor='w')
		return label

	def set_image(self, location, image, width=300, height=300):
		# if image is None
		# set default image is no_image
		if len(image) == 0:
			default_image_path = 'image/no_image.jpg' 
			image = cv2.imread(default_image_path)
		# resize and convert image to tkinter image type
		image = cv2.resize(image, (width, height))
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = Image.fromarray(image)
		image = ImageTk.PhotoImage(image)
		# check localion image and put image to label
		if location == 1:
			self.image1.configure(image=image)
			self.image1.image = image
		elif location == 2:
			self.image2.configure(image=image)
			self.image2.image = image
		elif location == 3:
			self.image3.configure(image=image)
			self.image3.image = image
		elif location == 4:
			self.image4.configure(image=image)
			self.image4.image = image
		elif location == 5:
			self.image5.configure(image=image)
			self.image5.image = image
		else:
			self.image6.configure(image=image)
			self.image6.image = image

	def show_alert(self):
		messagebox.showwarning("Infor", "Could not open file")

	def show_error(self):
		top = tk.Toplevel()
		top.title('ALERT')
		tk.Message(top, text="ERROR", padx=20, pady=20).pack()
		top.after(2000, top.destroy)

	def show_success(self):
		top = tk.Toplevel()
		top.title('ALERT')
		tk.Message(top, text="SUCCESS", padx=20, pady=20).pack()
		top.after(2000, top.destroy)




def main():
	master = tk.Tk()
	screen = Screen(master)
	screen.show_success()
	master.mainloop()


if __name__ == '__main__':
	main()

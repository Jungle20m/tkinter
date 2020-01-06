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
		self.create_container()
		self.create_screen_in()
		self.create_screen_out()

	def create_container(self):
		# Container
		self.l1 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.l2 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.l3 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.l4 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.l5 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.l6 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.l7 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.r1 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.r2 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.r3 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.r4 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.r5 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.r6 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		self.r7 = tk.Frame(self.master, borderwidth=2, relief='ridge')
		# layout container
		self.l1.grid(row=0, column=0, sticky="nsew")
		self.l2.grid(row=0, column=1, sticky="nsew")
		self.l3.grid(row=1, column=0, sticky="nsew")
		self.l4.grid(row=1, column=1, sticky="nsew")
		self.l5.grid(row=2, column=0, sticky="nsew")
		self.l6.grid(row=2, column=1, sticky="nsew")
		self.l7.grid(row=3, column=0, sticky="nsew", columnspan=2)
		self.r1.grid(row=0, column=2, sticky="nsew")
		self.r2.grid(row=0, column=3, sticky="nsew")
		self.r3.grid(row=1, column=2, sticky="nsew")
		self.r4.grid(row=1, column=3, sticky="nsew")
		self.r5.grid(row=2, column=2, sticky="nsew")
		self.r6.grid(row=2, column=3, sticky="nsew")
		self.r7.grid(row=3, column=2, sticky="nsew", columnspan=2)

	def create_screen_in(self):
		# Image
		self.image_l1 = self.create_image_label(self.l1, 200, 200)
		self.image_l2 = self.create_image_label(self.l2, 200, 200)
		self.image_l3 = self.create_image_label(self.l3, 200, 200)
		self.image_l4 = self.create_image_label(self.l4, 200, 200)
		self.image_l5 = self.create_image_label(self.l5, 200, 200)
		self.image_l6 = self.create_image_label(self.l6, 200, 200)
		# layout image
		self.image_l1.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_l2.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_l3.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_l4.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_l5.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_l6.pack(fill=tk.BOTH, expand=tk.YES)
		# Information
		l_label_name = self.create_infor_label(self.l7, "Họ tên:")
		l_label_position = self.create_infor_label(self.l7, "Vị trí:")
		l_label_plate_number = self.create_infor_label(self.l7, "Biển số xe:")
		l_label_timein = self.create_infor_label(self.l7, "Thời gian vào:")
		self.l_name = self.create_infor_label(self.l7, text="Nguyễn Văn Đức", font=("Helvetica", 12, 'bold'), width=20)
		self.l_position = self.create_infor_label(self.l7, "DEV", font=("Helvetica", 12, 'bold'), width=20)
		self.l_plate_number = self.create_infor_label(self.l7, "03829", font=("Helvetica", 12, 'bold'), width=20)
		self.l_timein = self.create_infor_label(self.l7, "07:13:21", font=("Helvetica", 12, 'bold'), width=20)
		# layout information
		l_label_name.grid(row=1, column=0, padx=20)
		l_label_position.grid(row=2, column=0, padx=20)
		l_label_plate_number.grid(row=3, column=0, padx=20)
		l_label_timein.grid(row=4, column=0, padx=20)
		self.l_name.grid(row=1, column=1, sticky='nesw')
		self.l_position.grid(row=2, column=1, sticky='nesw')
		self.l_plate_number.grid(row=3, column=1, sticky='nesw')
		self.l_timein.grid(row=4, column=1, sticky='nesw')
		
	def create_screen_out(self):
		# Image
		self.image_r1 = self.create_image_label(self.r1, 200, 200)
		self.image_r2 = self.create_image_label(self.r2, 200, 200)
		self.image_r3 = self.create_image_label(self.r3, 200, 200)
		self.image_r4 = self.create_image_label(self.r4, 200, 200)
		self.image_r5 = self.create_image_label(self.r5, 200, 200)
		self.image_r6 = self.create_image_label(self.r6, 200, 200)
		# layout image
		self.image_r1.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_r2.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_r3.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_r4.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_r5.pack(fill=tk.BOTH, expand=tk.YES)
		self.image_r6.pack(fill=tk.BOTH, expand=tk.YES)
		# Information
		r_label_name = self.create_infor_label(self.r7, "Họ tên:")
		r_label_position = self.create_infor_label(self.r7, "Vị trí:")
		r_label_plate_number = self.create_infor_label(self.r7, "Biển số xe:")
		r_label_timein = self.create_infor_label(self.r7, "Thời gian vào:")
		r_label_timeout = self.create_infor_label(self.r7, "Thời gian ra:")
		self.r_name = self.create_infor_label(self.r7, "Nguyễn Văn Đức", font=("Helvetica", 12, 'bold'), width=20)
		self.r_position = self.create_infor_label(self.r7, "DEV", font=("Helvetica", 12, 'bold'), width=20)
		self.r_plate_number = self.create_infor_label(self.r7, "03829", font=("Helvetica", 12, 'bold'), width=20)
		self.r_timein = self.create_infor_label(self.r7, "07:13:21", font=("Helvetica", 12, 'bold'), width=20)
		self.r_timeout = self.create_infor_label(self.r7, "18:06:03", font=("Helvetica", 12, 'bold'), width=20)
		# layout information
		r_label_name.grid(row=0, column=0, pady=0, padx=20, sticky=tk.W)
		r_label_position.grid(row=1, column=0, pady=0, padx=20, sticky=tk.W)
		r_label_plate_number.grid(row=2, column=0, pady=0, padx=20, sticky=tk.W)
		r_label_timein.grid(row=3, column=0, pady=0, padx=20, sticky=tk.W)
		r_label_timeout.grid(row=4, column=0, pady=0, padx=20, sticky=tk.W)
		self.r_name.grid(row=0, column=1, sticky=tk.W)
		self.r_position.grid(row=1, column=1, sticky=tk.W)
		self.r_plate_number.grid(row=2, column=1, sticky=tk.W)
		self.r_timein.grid(row=3, column=1, sticky=tk.W)
		self.r_timeout.grid(row=4, column=1, sticky=tk.W)

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

	def create_infor_label(self, container, text, font=("Helvetica", 12), fg="#282828", width=15):
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
		if location == 'l1':
			self.image_l1.configure(image=image)
			self.image_l1.image = image
		elif location == 'l2':
			self.image_l2.configure(image=image)
			self.image_l2.image = image
		elif location == 'l3':
			self.image_l3.configure(image=image)
			self.image_l3.image = image
		elif location == 'l4':
			self.image_l4.configure(image=image)
			self.image_l4.image = image
		elif location == 'l5':
			self.image_l5.configure(image=image)
			self.image_l5.image = image
		elif location == 'l6':
			self.image_l6.configure(image=image)
			self.image_l7.image = image
		elif location == 'r1':
			self.image_r1.configure(image=image)
			self.image_r1.image = image
		elif location == 'r2':
			self.image_r2.configure(image=image)
			self.image_r2.image = image
		elif location == 'r3':
			self.image_r3.configure(image=image)
			self.image_r3.image = image
		elif location == 'r4':
			self.image_r4.configure(image=image)
			self.image_r4.image = image
		elif location == 'r5':
			self.image_r5.configure(image=image)
			self.image_r5.image = image
		else:
			self.image_r6.configure(image=image)
			self.image_r6.image = image


def main():
	master = tk.Tk()
	screen = Screen(master)
	master.mainloop()


if __name__ == '__main__':
	main()




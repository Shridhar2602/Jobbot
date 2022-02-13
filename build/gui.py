from pathlib import Path
from tkinter.filedialog import askopenfilename
from turtle import update
import webbrowser
import os
import Scraper.scrap as sc
import build.build_resume.gui as gui2
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

str1 = os.path.dirname(__file__)

def build_resume():
	window.destroy()
	gui2.Start()
	window.quit()

def relative_to_assets(path: str) -> Path:
	return ASSETS_PATH / Path(path)

info = []

def get_list():
	global info
	password = entry_1.get()
	username = entry_2.get()
	info = sc.begin(username, password)
	window.destroy()
	window.quit()

filepath = ""

def get_filepath():
	global filepath
	filepath = askopenfilename(initialdir="~", title="Upload your resume")
	temp = filepath.split("/")
	print(filepath)
	canvas.itemconfigure(resume, text=temp[-1])
	
def Start():
	print("Starting Main GUI.....")
	global window, canvas, resume, entry_1, entry_2
	window = Tk(className="Jobbot")

	window.geometry("862x519")
	window.configure(bg = "#3A7FF6")

	canvas = Canvas(
		window,
		bg = "#3A7FF6",
		height = 519,
		width = 862,
		bd = 0,
		highlightthickness = 0,
		relief = "ridge"
	)

	canvas.place(x = 0, y = 0)
	image_image_1 = PhotoImage(
		file=relative_to_assets("image_1.png"))
	image_1 = canvas.create_image(
		215.0,
		259.0,
		image=image_image_1
	)

	canvas.create_rectangle(
		431.0,
		3.552713678800501e-15,
		862.0,
		519.0,
		fill="#FFFFFF",
		outline="")

	button_image_1 = PhotoImage(
		file=relative_to_assets("button_1.png"))
	button_1 = Button(
		image=button_image_1,
		borderwidth=0,
		highlightthickness=0,
		command=lambda: get_list(),
		relief="flat"
	)
	button_1.place(
		x=555.0,
		y=396.0,
		width=180.0,
		height=55.0
	)

	button_image_2 = PhotoImage(
		file=relative_to_assets("button_2.png"))

	button_2= canvas.create_image(151.99999999999997, 466.0, anchor="nw",image=button_image_2)
	canvas.tag_bind(button_2, "<Button-1>", lambda x: webbrowser.open_new_tab('https://github.com/Shridhar2602/Jobbot'))

	image_image_2 = PhotoImage(
		file=relative_to_assets("image_2.png"))
	image_2 = canvas.create_image(
		646.0,
		35.0,
		image=image_image_2
	)

	entry_image_1 = PhotoImage(
		file=relative_to_assets("entry_1.png"))
	entry_bg_1 = canvas.create_image(
		645.0,
		241.0,
		image=entry_image_1
	)
	entry_1 = Entry(
		bd=0,
		bg="#ECECF5",
		highlightthickness=0,
		show="*"
	)

	entry_1.place(
		x=478.0,
		y=213.0,
		width=300.0,
		height=54.0
	)

	entry_image_2 = PhotoImage(
		file=relative_to_assets("entry_2.png"))
	entry_bg_2 = canvas.create_image(
		645.0,
		166.0,
		image=entry_image_2
	)
	entry_2 = Entry(
		bd=0,
		bg="#ECECF5",
		highlightthickness=0
	)
	entry_2.place(
		x=478.0,
		y=138.0,
		width=300.0,
		height=54.0
	)

	canvas.create_rectangle(
		185.0,
		85.0,
		245.0,
		90.0,
		fill="#FCFCFC",
		outline="")

	image_image_3 = PhotoImage(
		file=relative_to_assets("image_3.png"))
	image_3 = canvas.create_image(
		591.0,
		112.0,
		image=image_image_3
	)

	image_image_4 = PhotoImage(
		file=relative_to_assets("image_4.png"))
	image_4 = canvas.create_image(
		214.0,
		64.0,
		image=image_image_4
	)

	image_image_5 = PhotoImage(
		file=relative_to_assets("image_5.png"))
	image_5 = canvas.create_image(
		215.0,
		125.0,
		image=image_image_5
	)

	canvas.create_text(
		443.0,
		475.0,
		anchor="nw",
		text="Your password is safe, secure, and protected.",
		fill="#807C7C",
		font=("Roboto Bold", 15 * -1)
	)

	canvas.create_text(
		443.0,
		493.0,
		anchor="nw",
		text="We do not store your confidential data.",
		fill="#807C7C",
		font=("Roboto Bold", 15 * -1)
	)

	image_image_6 = PhotoImage(
		file=relative_to_assets("image_6.png"))
	image_6 = canvas.create_image(
		795.0,
		166.0,
		image=image_image_6
	)

	image_image_7 = PhotoImage(
		file=relative_to_assets("image_7.png"))
	image_7 = canvas.create_image(
		795.0,
		238.0,
		image=image_image_7
	)

	# Uplaod file
	button_image_3 = PhotoImage(
		file=relative_to_assets("button_3.png"))
	button_3 = Button(
		image=button_image_3,
		borderwidth=0,
		highlightthickness=0,
		command=lambda: get_filepath(),
		relief="flat"
	)

	button_3.place(
		x=468.0,
		y=288.0,
		width=219.0,
		height=56.0
	)

	resume = canvas.create_text(
		711.0,
		303.0,
		anchor="nw",
		text=filepath,
		fill="#000000",
		font=("Noto Sans", 19 * -1)
	)

	canvas.create_text(
		185.0,
		451.0,
		anchor="nw",
		text="Find us on ",
		fill="#FFFFFF",
		font=("Arsenal Regular", 15 * -1)
	)

	image_image_8 = PhotoImage(
		file=relative_to_assets("image_8.png"))
	image_8 = canvas.create_image(
		215.0,
		254.0,
		image=image_image_8
	)

	canvas.create_text(
		511.0,
		360.0,
		anchor="nw",
		text="Don’t have a Resume?",
		fill="#000000",
		font=("Noto Sans", 15 * -1)
	)

	button_image_4 = PhotoImage(
		file=relative_to_assets("button_4.png"))
	button_4 = Button(
		image=button_image_4,
		borderwidth=0,
		highlightthickness=0,
		command=lambda: build_resume(),
		relief="flat"
	)

	button_4.place(
		x=688.0,
		y=356.0,
		width=83.0,
		height=20.0
	)

	window.resizable(True, True)
	window.mainloop()

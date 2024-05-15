from tkinter import Tk, Label, Button, Checkbutton, Radiobutton, Entry, Grid, messagebox
from tkinter.ttk import Progressbar

def buttonClicked(window: Tk, name: str):
	p: Progressbar = window.nametowidget("progress")
	x = p["value"]
	p.config(value=x + 1)
	
	# e: Entry = window.nametowidget("input")
	# l: Label = window.nametowidget("output")
	# l.config(text=e.get())
	
	# answer = messagebox.askyesno(title="Eine Frage", message="Möchtest du begrüßt werden?")
	# if answer:
	# 	component = window.nametowidget(name)
	# 	if type(component) == Label:
	# 		l: Label = component
	# 		l.config(text="Hallo")

window = Tk()
window.wm_title("Meine dritte Python GUI")
window.geometry("600x300+-1000+300")
window.config(background="green")

button = Button(text="Mein Button")
button.grid(column=1, row=1)
# button.place(width=100, height=50, x=250, y=225)
# def anon():
# 	buttonClicked(window, "output")
button.config(command=lambda: buttonClicked(window, "output"))

label = Label(background="white", name="output")
label.grid(row=0, columnspan=10)
label.columnconfigure(0)
# label.place(width=500, height=150, x=50, y=50)
label.config(font=("Arial", 40), fg="orange")

for c in range(3):
	check = Checkbutton(text=f"Test{c}", name=f"checkbox{c}")
	check.grid(row=1, column=0)
	# check.place(x=50 + (c * 55), y=225)

for c in range(3):
	radio = Radiobutton(text=f"Test{c}", name=f"radiobutton{c}", value=c)  # indicatoron=False
	radio.grid(row=1, column=0)
	# radio.place(x=50 + (c * 55), y=245)

entry = Entry(name="input")
entry.grid(column=2, row=1)
# entry.place(x=400, y=225, width=150, height=20)

progress = Progressbar(maximum=100, value=0, name="progress")
entry.grid(column=2, row=1)
# progress.place(x=400, y=250, width=150, height=20)

window.mainloop()
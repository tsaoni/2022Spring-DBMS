from tkinter import *
from tkinter import messagebox
from query import query_page
from button import button_page

def main_page():
	# main page element declaration
	## title
	title = Label(text="Welcome to App market DataBase!", font=("Arial", 20))
	subtitle = Label(text="Please select an option to make your query...", font=("Arial", 10))
	## checkbox
	qvar = IntVar()
	bvar = IntVar()
	qcb = Checkbutton(root, text='query',variable=qvar, onvalue=1, offvalue=0)
	bcb = Checkbutton(root, text='button',variable=bvar, onvalue=1, offvalue=0)
	## button
	button_ok = Button(root, text="Select", command=lambda: on_selection(qvar, bvar, mp_elements))
	button_quit = Button(root, text="Exit", command=root.quit)
	## main page elements
	mp_elements = [title, subtitle, qcb, bcb, button_ok, button_quit] 

	# main page element position
	title.grid(row= 0, column=0)
	subtitle.grid(row=1, column=0)
	qcb.grid(row=2, column=0)
	bcb.grid(row=3, column=0)
	button_ok.grid(row=4, column=0)
	button_quit.grid(row=5, column=0)

# main page selection case
def on_selection(qvar, bvar, mp_elements):
	if (qvar.get() == 1) & (bvar.get() == 0):
		exit_main('q', mp_elements)
	elif (qvar.get() == 0) & (bvar.get() == 1):
		exit_main('b', mp_elements)
	elif (qvar.get() == 0) & (bvar.get() == 0):
		messagebox.showerror("Error", "Please select query or button!")
	else:
		messagebox.showerror("Error", "Please select ONE of the options!")
 
# leave main page
def exit_main(op, mp_elements):
	for emt in mp_elements:
		emt.destroy()
	if op == 'q':
		query_page(root)
	else:
		button_page(root)

if __name__ == '__main__':
	# start program
	root = Tk()
	root.title('App market DataBase system')
	root.geometry('500x250')
	main_page()
	# looping...
	root.mainloop()
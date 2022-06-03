from tkinter import *
import sys
import os

def restart_program(root):
	python = sys.executable
	os.execl(python, python, * sys.argv)

def op_interface(root, op, q_elements):
	for e in q_elements:
		e.destroy()
	otitle = Label(text="Please select the conditions:", font=("Arial", 10))

	if op == "SELECT-FROM-WHERE":
		pass
	elif op == "DELETE":
		pass
	elif op == "INSERT":
		pass
	elif op == "UPDATE":
		pass
	elif op == "IN":
		pass
	elif op == "NOT IN":
		pass
	elif op == "EXISTS":
		pass
	elif op == "COUNT":
		pass
	elif op == "SUM":
		pass
	elif op == "MAX":
		pass
	elif op == "MIN":
		pass
	elif op == "AVG":
		pass
	else: # op == "HAVING"
		pass

	ok_button = Button(root, text="ok", command=show_result)
	back_button = Button(root, text="restart", command=lambda: restart_program(root))
	
	otitle.grid(row=0, column=0)
	ok_button.grid(row=1, column=0)
	back_button.grid(row=2, column=0)

	return

def show_result():
	pass

def button_page(root):
	# button page element declaration
	btitle = Label(text="Please select options", font=("Arial", 10))
	ok_button = Button(root, text="ok", command=lambda: op_interface(root, op_value.get(), q_elements))
	back_button = Button(root, text="restart", command=lambda: restart_program(root))
	op_value = StringVar(root)
	menu = OptionMenu(root, op_value, "SELECT-FROM-WHERE", 
				   "DELETE", "INSERT", "UPDATE", 
				   "IN", "NOT IN", "EXISTS", 
				   "NOT EXISTS", "COUNT", "SUM", 
				   "MAX", "MIN", "AVG", "HAVING")
	q_elements = [btitle, ok_button, back_button, menu]

	# button page element position
	btitle.grid(row=0, column=0)
	menu.grid(row=1, column=0)
	ok_button.grid(row=2, column=0)
	back_button.grid(row=3, column=0)

	op_value.set("SELECT-FROM-WHERE") # default value
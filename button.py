from tkinter import *
import sqlite3
import sys
import os

def restart_program(root):
	python = sys.executable
	os.execl(python, python, * sys.argv)

def op_interface(root, op, q_elements):
	for e in q_elements:
		e.destroy()
	# otitle = Label(text="Please select the conditions:", font=("Arial", 10))

	if op == "SELECT-FROM-WHERE":
		SELECT_FROM_WHERE()
	elif op == "DELETE":
		DELETE()
	elif op == "INSERT":
		INSERT(root, 0)
	elif op == "UPDATE":
		UPDATE()
	elif op == "IN":
		IN()
	elif op == "NOT IN":
		NOT_IN()
	elif op == "EXISTS":
		EXISTS()
	elif op == "COUNT":
		COUNT()
	elif op == "SUM":
		SUM()
	elif op == "MAX":
		MAX()
	elif op == "MIN":
		MIN()
	elif op == "AVG":
		AVG()
	else: # op == "HAVING"
		HAVING()

	
	back_button = Button(root, text="restart", command=lambda: restart_program(root))
	
	# otitle.grid(row=0, column=0)
	back_button.grid(row=11, column=0)

	return
"""
def show_result():
	# database
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	# execute sql script
	c.execute("INSERT INTO company (COMPANY_ID, COMPANY_NAME, IS_INTERNATIONAL) VALUES(?, ?, ?)",
			  [id_entry.get(), name_entry.get(), value.get()])
	print(c.execute("SELECT * FROM COMPANY").fetchall())
	conn.commit()
	conn.close()
"""

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

# SQL operation
def SELECT_FROM_WHERE():
	pass

def DELETE():
	pass
	

def INSERT(root, page, ele = None, table = None):
	# choose the table to insert
	if page == 0:
		title = Label(text="Please choose a table to insert:", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "COMPANY", 
					   "DEVELOPER", "APP", "PLATFORM", 
					   "CLIENT", "TRADE", "REPORT_BUG")
		value.set("COMPANY") # default value
		ok_button = Button(root, text="next", command=lambda: INSERT(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# insert conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# insert elements in new page
		if table == "COMPANY":
			company(root, "INSERT", 0)
			f = lambda: company(root, "INSERT", 1)
		elif table == "DEVELOPER":
			developer("INSERT", 0)
			f = lambda: developer("INSERT", 1)
		elif table == "APP":
			APP("INSERT", 0)
			f = lambda: APP("INSERT", 1)
		elif table == "PLATFORM":
			platform("INSERT", 0)
			f = lambda: platform("INSERT", 1)
		elif table == "CLIENT":
			client("INSERT", 0)
			f = lambda: client("INSERT", 1)
		elif table == "TRADE":
			trade("INSERT", 0)
			f = lambda: trade("INSERT", 1)
		else: # table == "REPORT_BUG"
			report_bug("INSERT", 0)
			f = lambda: report_bug("INSERT", 1)

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)



def UPDATE():
	pass

def IN():
	pass

def NOT_IN():
	pass

def EXISTS():
	pass

def COUNT():
	pass

def SUM():
	pass

def MAX():
	pass

def MIN():
	pass

def AVG():
	pass

def HAVING():
	pass

# table operation
company_element = []
def company(root, op, page):
	global company_element
	if op == "INSERT":
		if page == 0:
			# GUI
			id_label = Label(text="Company ID", font=("Arial", 10))
			name_label = Label(text="Company Name", font=("Arial", 10))
			inter_label = Label(text="is international?", font=("Arial", 10))
			id_entry = Entry(root, width=30)
			name_entry = Entry(root, width=30)
			company_element.append(id_entry)
			company_element.append(name_entry)
			value = StringVar(root)
			company_element.append(value)
			is_international = OptionMenu(root, value, "yes", "no")
			value.set("yes") # default value

			id_label.grid(row=0, column=0)
			id_entry.grid(row=1, column=0)
			name_label.grid(row=2, column=0)
			name_entry.grid(row=3, column=0)
			inter_label.grid(row=4, column=0)
			is_international.grid(row=5, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute("INSERT INTO company (COMPANY_ID, COMPANY_NAME, IS_INTERNATIONAL) VALUES(?, ?, ?)",
					 [company_element[0].get(), company_element[1].get(), company_element[2].get()])
			print(c.execute("SELECT * FROM COMPANY").fetchall())
			conn.commit()
			conn.close()
			company_element[0].delete(0, END)
			company_element[1].delete(0, END)

def developer(op):
	pass

def APP(op):
	pass

def platform(op):
	pass

def client(op):
	pass

def trade(op):
	pass

def report_bug(op):
	pass
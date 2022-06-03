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
		DELETE(root, 0)
	elif op == "INSERT":
		INSERT(root, 0)
	elif op == "UPDATE":
		UPDATE(root, 0)
	elif op == "IN":
		IN(root, 0)
	elif op == "NOT IN":
		NOT_IN(root, 0)
	elif op == "EXISTS":
		EXISTS(root, 0)
	elif op == "NOT EXISTS":
		NOT_EXISTS()
	elif op == "COUNT":
		COUNT()
	elif op == "SUM":
		SUM(root, 0)
	elif op == "MAX":
		MAX(root, 0)
	elif op == "MIN":
		MIN(root, 0)
	elif op == "AVG":
		AVG(root, 0)
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

def DELETE(root, page, ele = None, table = None):
	# choose the table to delete
	if page == 0:
		title = Label(text="Please choose a table to delete:", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "COMPANY", 
					   "DEVELOPER", "APP", "PLATFORM", 
					   "CLIENT", "TRADE", "REPORT_BUG")
		value.set("COMPANY") # default value
		ok_button = Button(root, text="next", command=lambda: DELETE(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# delete conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# delete elements in new page
		if table == "COMPANY":
			company(root, "DELETE", 0)
			f = lambda: company(root, "DELETE", 1)
		elif table == "DEVELOPER":
			developer("DELETE", 0)
			f = lambda: developer("DELETE", 1)
		elif table == "APP":
			APP(root, "DELETE", 0)
			f = lambda: APP(root, "DELETE", 1)
		elif table == "PLATFORM":
			platform("DELETE", 0)
			f = lambda: platform("DELETE", 1)
		elif table == "CLIENT":
			client("DELETE", 0)
			f = lambda: client("DELETE", 1)
		elif table == "TRADE":
			trade("DELETE", 0)
			f = lambda: trade("DELETE", 1)
		else: # table == "REPORT_BUG"
			report_bug("DELETE", 0)
			f = lambda: report_bug("DELETE", 1)

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

	

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
			APP(root, "INSERT", 0)
			f = lambda: APP(root, "INSERT", 1)
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



def UPDATE(root, page, ele = None, table = None):
	# choose the table to update
	if page == 0:
		title = Label(text="Please choose a table to update:", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "COMPANY", 
					   "DEVELOPER", "APP", "PLATFORM", 
					   "CLIENT", "TRADE", "REPORT_BUG")
		value.set("COMPANY") # default value
		ok_button = Button(root, text="next", command=lambda: UPDATE(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# update conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# update elements in new page
		if table == "COMPANY":
			company(root, "UPDATE", 0)
			f = lambda: company(root, "UPDATE", 1)
		elif table == "DEVELOPER":
			developer("UPDATE", 0)
			f = lambda: developer("UPDATE", 1)
		elif table == "APP":
			APP(root, "UPDATE", 0)
			f = lambda: APP(root, "UPDATE", 1)
		elif table == "PLATFORM":
			platform("UPDATE", 0)
			f = lambda: platform("UPDATE", 1)
		elif table == "CLIENT":
			client("UPDATE", 0)
			f = lambda: client("UPDATE", 1)
		elif table == "TRADE":
			trade("UPDATE", 0)
			f = lambda: trade("UPDATE", 1)
		else: # table == "REPORT_BUG"
			report_bug("UPDATE", 0)
			f = lambda: report_bug("UPDATE", 1)

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

def IN(root, page, ele = None, table = None):
	# choose the table to delete
	if page == 0:
		title = Label(text="Please choose a relationship to do 'in':", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "work for", 
					   "release", "trade", "report bug")
		value.set("work for") # default value
		ok_button = Button(root, text="next", command=lambda: IN(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# delete conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# delete elements in new page
		if table == "work for":
			Work_for()
			f = lambda: Work_for()
		elif table == "release":
			Release(root, "IN", 0)
			f = lambda: Release(root, "IN", 1)
		elif table == "trade":
			Trade()
			f = lambda: Trade()
		else: # table == "report bug":
			Report_bug()
			f = lambda: Report_bug()

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

def NOT_IN(root, page, ele = None, table = None):
	# choose the table to delete
	if page == 0:
		title = Label(text="Please choose a relationship to do 'not in':", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "work for", 
					   "release", "trade", "report bug")
		value.set("work for") # default value
		ok_button = Button(root, text="next", command=lambda: NOT_IN(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# delete conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# delete elements in new page
		if table == "work for":
			Work_for()
			f = lambda: Work_for()
		elif table == "release":
			Release(root, "NOT_IN", 0)
			f = lambda: Release(root, "NOT_IN", 1)
		elif table == "trade":
			Trade()
			f = lambda: Trade()
		else: # table == "report bug":
			Report_bug()
			f = lambda: Report_bug()

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

def EXISTS(root, page, ele = None, table = None):
	# choose the table to delete
	if page == 0:
		title = Label(text="Please choose a relationship to do 'exists':", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "work for", 
					   "release", "trade", "report bug")
		value.set("work for") # default value
		ok_button = Button(root, text="next", command=lambda: EXISTS(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# delete conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# delete elements in new page
		if table == "work for":
			Work_for()
			f = lambda: Work_for()
		elif table == "release":
			Release(root, "EXISTS", 0)
			f = lambda: Release(root, "EXISTS", 1)
		elif table == "trade":
			Trade()
			f = lambda: Trade()
		else: # table == "report bug":
			Report_bug()
			f = lambda: Report_bug()

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

def NOT_EXISTS():
	pass

def COUNT():
	pass

def SUM(root, page, ele = None, table = None):
	# choose the table to do sum
	if page == 0:
		title = Label(text="Please choose a table to do sum:", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "COMPANY", 
					   "DEVELOPER", "APP", "PLATFORM", 
					   "CLIENT", "TRADE", "REPORT_BUG")
		value.set("COMPANY") # default value
		ok_button = Button(root, text="next", command=lambda: SUM(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# do sum conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# do sum in new page
		if table == "COMPANY":
			company(root, "SUM", 0)
			f = lambda: company(root, "SUM", 1)
		elif table == "DEVELOPER":
			developer("SUM", 0)
			f = lambda: developer("SUM", 1)
		elif table == "APP":
			APP(root, "SUM", 0)
			f = lambda: APP(root, "SUM", 1)
		elif table == "PLATFORM":
			platform("SUM", 0)
			f = lambda: platform("SUM", 1)
		elif table == "CLIENT":
			client("SUM", 0)
			f = lambda: client("SUM", 1)
		elif table == "TRADE":
			trade("SUM", 0)
			f = lambda: trade("SUM", 1)
		else: # table == "REPORT_BUG"
			report_bug("SUM", 0)
			f = lambda: report_bug("SUM", 1)

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

def MAX(root, page, ele = None, table = None):
	# choose the table to do sum
	if page == 0:
		title = Label(text="Please choose a table to do max:", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "COMPANY", 
					   "DEVELOPER", "APP", "PLATFORM", 
					   "CLIENT", "TRADE", "REPORT_BUG")
		value.set("COMPANY") # default value
		ok_button = Button(root, text="next", command=lambda: MAX(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# do sum conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# do sum in new page
		if table == "COMPANY":
			company(root, "MAX", 0)
			f = lambda: company(root, "MAX", 1)
		elif table == "DEVELOPER":
			developer("MAX", 0)
			f = lambda: developer("MAX", 1)
		elif table == "APP":
			APP(root, "MAX", 0)
			f = lambda: APP(root, "MAX", 1)
		elif table == "PLATFORM":
			platform("MAX", 0)
			f = lambda: platform("MAX", 1)
		elif table == "CLIENT":
			client("MAX", 0)
			f = lambda: client("MAX", 1)
		elif table == "TRADE":
			trade("MAX", 0)
			f = lambda: trade("MAX", 1)
		else: # table == "REPORT_BUG"
			report_bug("MAX", 0)
			f = lambda: report_bug("MAX", 1)

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

def MIN(root, page, ele = None, table = None):
	# choose the table to do sum
	if page == 0:
		title = Label(text="Please choose a table to do min:", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "COMPANY", 
					   "DEVELOPER", "APP", "PLATFORM", 
					   "CLIENT", "TRADE", "REPORT_BUG")
		value.set("COMPANY") # default value
		ok_button = Button(root, text="next", command=lambda: MIN(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# do sum conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# do sum in new page
		if table == "COMPANY":
			company(root, "MIN", 0)
			f = lambda: company(root, "MIN", 1)
		elif table == "DEVELOPER":
			developer("MIN", 0)
			f = lambda: developer("MIN", 1)
		elif table == "APP":
			APP(root, "MIN", 0)
			f = lambda: APP(root, "MIN", 1)
		elif table == "PLATFORM":
			platform("MIN", 0)
			f = lambda: platform("MIN", 1)
		elif table == "CLIENT":
			client("MIN", 0)
			f = lambda: client("MIN", 1)
		elif table == "TRADE":
			trade("MIN", 0)
			f = lambda: trade("MIN", 1)
		else: # table == "REPORT_BUG"
			report_bug("MIN", 0)
			f = lambda: report_bug("MIN", 1)

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

def AVG(root, page, ele = None, table = None):
	# choose the table to do sum
	if page == 0:
		title = Label(text="Please choose a table to do average:", font=("Arial", 10))
		value = StringVar(root)
		menu = OptionMenu(root, value, "COMPANY", 
					   "DEVELOPER", "APP", "PLATFORM", 
					   "CLIENT", "TRADE", "REPORT_BUG")
		value.set("COMPANY") # default value
		ok_button = Button(root, text="next", command=lambda: AVG(root, 1, elements, value.get()))
		elements = [title, menu, ok_button]

		title.grid(row=0, column=0)
		menu.grid(row=1, column=0)
		ok_button.grid(row=2, column=0)

	# do sum conditions
	elif page == 1:
		# delete elements from last page
		for e in ele:
			e.destroy()
		f = None
		# do sum in new page
		if table == "COMPANY":
			company(root, "AVG", 0)
			f = lambda: company(root, "AVG", 1)
		elif table == "DEVELOPER":
			developer("AVG", 0)
			f = lambda: developer("AVG", 1)
		elif table == "APP":
			APP(root, "AVG", 0)
			f = lambda: APP(root, "AVG", 1)
		elif table == "PLATFORM":
			platform("AVG", 0)
			f = lambda: platform("AVG", 1)
		elif table == "CLIENT":
			client("AVG", 0)
			f = lambda: client("AVG", 1)
		elif table == "TRADE":
			trade("AVG", 0)
			f = lambda: trade("AVG", 1)
		else: # table == "REPORT_BUG"
			report_bug("AVG", 0)
			f = lambda: report_bug("AVG", 1)

		ok_button = Button(root, text="ok", command= f)
		ok_button.grid(row=10, column=0)

def HAVING():
	pass

# table operation
company_element = []
def company(root, op, page):
	global company_element
	if op == "INSERT":
		if page == 0:
			# GUI
			company_element = []
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
			c.execute("INSERT INTO COMPANY (COMPANY_ID, COMPANY_NAME, IS_INTERNATIONAL) VALUES(?, ?, ?)",
					 [company_element[0].get(), company_element[1].get(), company_element[2].get()])
			print(c.execute("SELECT * FROM COMPANY").fetchall())
			conn.commit()
			conn.close()
			company_element[0].delete(0, END)
			company_element[1].delete(0, END)

	if op == "DELETE":
		if page == 0:
			# GUI
			company_element = []
			name_label = Label(text="Type the Company Name to delete", font=("Arial", 10))
			name_entry = Entry(root, width=30)
			company_element.append(name_entry)

			name_label.grid(row=0, column=0)
			name_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute("DELETE FROM COMPANY WHERE COMPANY_NAME = ?",
					 [company_element[0].get()])
			print(c.execute("SELECT * FROM COMPANY").fetchall())
			conn.commit()
			conn.close()
			company_element[0].delete(0, END)

	if op == "UPDATE":
		if page == 0:
			# GUI
			company_element = []
			id_label = Label(text="Please type Company ID to update", font=("Arial", 10))
			name_label = Label(text="Please type the new Company Name", font=("Arial", 10))
			id_entry = Entry(root, width=30)
			name_entry = Entry(root, width=30)
			company_element.append(id_entry)
			company_element.append(name_entry)

			id_label.grid(row=0, column=0)
			id_entry.grid(row=1, column=0)
			name_label.grid(row=2, column=0)
			name_entry.grid(row=3, column=0)
			
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute("UPDATE COMPANY SET COMPANY_NAME = ? WHERE COMPANY_ID = ?",
					 [company_element[1].get(), company_element[0].get()])
			print(c.execute("SELECT * FROM COMPANY").fetchall())
			conn.commit()
			conn.close()
			company_element[0].delete(0, END)
			company_element[1].delete(0, END)

def developer(op):
	pass

APP_element = []
def APP(root, op, page):
	global APP_element
	if op == "INSERT":
		if page == 0:
			# GUI
			APP_element = []
			id_label = Label(text="APP ID", font=("Arial", 10))
			cost_label = Label(text="APP Cost", font=("Arial", 10))
			install_label = Label(text="APP install number", font=("Arial", 10))
			company_label = Label(text="APP company ID", font=("Arial", 10))
			id_entry = Entry(root, width=30)
			cost_entry = Entry(root, width=30)
			install_entry = Entry(root, width=30)
			company_entry = Entry(root, width=30)
			APP_element.append(id_entry)
			APP_element.append(cost_entry)
			APP_element.append(install_entry)
			APP_element.append(company_entry)

			id_label.grid(row=0, column=0)
			id_entry.grid(row=1, column=0)
			cost_label.grid(row=2, column=0)
			cost_entry.grid(row=3, column=0)
			install_label.grid(row=4, column=0)
			install_entry.grid(row=5, column=0)
			company_label.grid(row=6, column=0)
			company_entry.grid(row=7, column=0)

		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute("INSERT INTO APP (APP_ID, INSTALL_NUM, COST, RELEASE_ID) VALUES(?, ?, ?, ?)",
					 [APP_element[0].get(), int(APP_element[2].get()), int(APP_element[1].get()), APP_element[3].get()])
			print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			APP_element[0].delete(0, END)
			APP_element[1].delete(0, END)
			APP_element[2].delete(0, END)
			APP_element[3].delete(0, END)

	if op == "DELETE":
		if page == 0:
			# GUI
			APP_element = []
			id_label = Label(text="Type the APP ID to delete", font=("Arial", 10))
			id_entry = Entry(root, width=30)
			APP_element.append(id_entry)

			id_label.grid(row=0, column=0)
			id_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute("DELETE FROM APP WHERE APP_ID = ?",
					 [APP_element[0].get()])
			print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			APP_element[0].delete(0, END)

	if op == "UPDATE":
		if page == 0:
			# GUI
			APP_element = []
			id_label = Label(text="Please type APP ID to update", font=("Arial", 10))
			cost_label = Label(text="Please type the new APP Cost", font=("Arial", 10))
			company_label = Label(text="Please type the new APP company ID", font=("Arial", 10))
			id_entry = Entry(root, width=30)
			cost_entry = Entry(root, width=30)
			company_entry = Entry(root, width=30)
			APP_element.append(id_entry)
			APP_element.append(cost_entry)
			APP_element.append(company_entry)

			id_label.grid(row=0, column=0)
			id_entry.grid(row=1, column=0)
			cost_label.grid(row=2, column=0)
			cost_entry.grid(row=3, column=0)
			company_label.grid(row=4, column=0)
			company_entry.grid(row=5, column=0)

		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute("UPDATE APP SET COST = ?, RELEASE_ID = ? WHERE APP_ID = ?",
					 [int(APP_element[1].get()), APP_element[2].get(), APP_element[0].get()])
			print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			APP_element[0].delete(0, END)
			APP_element[1].delete(0, END)
			APP_element[2].delete(0, END)

	if op == "SUM":
		if page == 0:
			# GUI
			APP_element = []
			company_label = Label(text="Type the company ID to get sum of APP install number", font=("Arial", 10))
			company_entry = Entry(root, width=30)
			APP_element.append(company_entry)
			company_label.grid(row=0, column=0)
			company_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			print(c.execute("SELECT RELEASE_ID, SUM(INSTALL_NUM) AS SUM_TABLE FROM APP WHERE RELEASE_ID = ?",
					 [APP_element[0].get()]).fetchall())
			# print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			APP_element[0].delete(0, END)

	if op == "MAX":
		if page == 0:
			# GUI
			APP_element = []
			company_label = Label(text="Type the company ID to get max of APP install number", font=("Arial", 10))
			company_entry = Entry(root, width=30)
			APP_element.append(company_entry)
			company_label.grid(row=0, column=0)
			company_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			print(c.execute("SELECT RELEASE_ID, MAX(INSTALL_NUM) AS SUM_TABLE FROM APP WHERE RELEASE_ID = ?",
					 [APP_element[0].get()]).fetchall())
			# print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			APP_element[0].delete(0, END)

	if op == "MIN":
		if page == 0:
			# GUI
			APP_element = []
			company_label = Label(text="Type the company ID to get min of APP install number", font=("Arial", 10))
			company_entry = Entry(root, width=30)
			APP_element.append(company_entry)
			company_label.grid(row=0, column=0)
			company_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			print(c.execute("SELECT RELEASE_ID, MIN(INSTALL_NUM) AS SUM_TABLE FROM APP WHERE RELEASE_ID = ?",
					 [APP_element[0].get()]).fetchall())
			# print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			APP_element[0].delete(0, END)

	if op == "AVG":
		if page == 0:
			# GUI
			APP_element = []
			company_label = Label(text="Type the company ID to get average of APP install number", font=("Arial", 10))
			company_entry = Entry(root, width=30)
			APP_element.append(company_entry)
			company_label.grid(row=0, column=0)
			company_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			print(c.execute("SELECT RELEASE_ID, AVG(INSTALL_NUM) AS SUM_TABLE FROM APP WHERE RELEASE_ID = ?",
					 [APP_element[0].get()]).fetchall())
			# print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			APP_element[0].delete(0, END)

def platform(op):
	pass

def client(op):
	pass

def trade(op):
	pass

def report_bug(op):
	pass

# relationship operation
def Work_for():
	pass

release_element = []
def Release(root, op, page):
	global release_element
	if op == "IN":
		if page == 0:
			# GUI
			release_element = []
			company_label = Label(text="Type the company Name to get all released APP ID", font=("Arial", 10))
			company_entry = Entry(root, width=30)
			release_element.append(company_entry)
			company_label.grid(row=0, column=0)
			company_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute('''PRAGMA foreign_keys = ON''')
			print(c.execute("SELECT APP_ID from APP WHERE RELEASE_ID IN (SELECT COMPANY_ID FROM COMPANY WHERE COMPANY_NAME = ?)",
					 [release_element[0].get()]).fetchall())
			# print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			release_element[0].delete(0, END)

	if op == "NOT_IN":
		if page == 0:
			# GUI
			release_element = []
			company_label = Label(text="Get all released APP ID except for the typed company", font=("Arial", 10))
			company_entry = Entry(root, width=30)
			release_element.append(company_entry)
			company_label.grid(row=0, column=0)
			company_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute('''PRAGMA foreign_keys = ON''')
			print(c.execute("SELECT APP_ID from APP WHERE RELEASE_ID NOT IN (SELECT COMPANY_ID FROM COMPANY WHERE COMPANY_NAME = ?)",
					 [release_element[0].get()]).fetchall())
			# print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			release_element[0].delete(0, END)

	if op == "EXISTS":
		if page == 0:
			# GUI
			release_element = []
			company_label = Label(text="Please type company name to see if it has released APP", font=("Arial", 10))
			company_entry = Entry(root, width=30)
			release_element.append(company_entry)
			company_label.grid(row=0, column=0)
			company_entry.grid(row=1, column=0)
		if page == 1:
			# database
			conn = sqlite3.connect('database.db')
			c = conn.cursor()
			# execute sql script
			c.execute('''PRAGMA foreign_keys = ON''')
			print(c.execute("SELECT APP_ID from APP WHERE EXISTS (SELECT * FROM COMPANY WHERE COMPANY.COMPANY_ID = APP.RELEASE_ID AND COMPANY_NAME = ?)",
					 [release_element[0].get()]).fetchall())
			# print(c.execute("SELECT * FROM APP").fetchall())
			conn.commit()
			conn.close()
			release_element[0].delete(0, END)

def Trade():
	pass

def Report_bug():
	pass
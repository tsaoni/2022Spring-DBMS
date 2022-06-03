from tkinter import *
import sqlite3
import sys
import os

def restart_program(root):
	python = sys.executable
	os.execl(python, python, * sys.argv)

def execute_sql(qentry):
	script = qentry.get()
	qentry.delete(0, END)

	# connect database
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	# execute sql script
	c.execute('''PRAGMA foreign_keys = ON''')
	c.execute(script)
	print(c.execute("SELECT * FROM COMPANY").fetchall())
	conn.commit()
	conn.close()

	return

def query_page(root):
	# query page element declaration
	qtitle = Label(text="Please enter SQL", font=("Arial", 10))
	qentry = Entry(root, width=50)
	get_button = Button(root, text="execute", command=lambda: execute_sql(qentry))
	back_button = Button(root, text="restart", command=lambda: restart_program(root))

	# query page element position
	qtitle.grid(row=0, column=0, columnspan=2)
	qentry.grid(row=1, column=0, columnspan=2)
	get_button.grid(row=2, column=0)
	back_button.grid(row=2, column=1)
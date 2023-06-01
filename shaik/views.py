from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

def home(r):
	return render(r,"home.html")

def contact(r):
	return render(r,"contact.html")

def books(r):
	return render(r,"books.html")

def about(req):
	con = sqlite3.connect("db.sqlite3")
	cur = con.cursor()
	res = cur.execute("SELECT name from sqlite_master")
	tables = res.fetchall()
	if ('books',) not in tables:
		 cur.execute("""CREATE table books
		 (id INTEGER NOT NULL,
		 book TEXT NOT NULL,
		 year INT NULL,
		 price INT NULL,
		 PRIMARY KEY("id" AUTOINCREMENT)
		 );""")


	if req.POST.get("add_book"):

		book = req.POST.get("book")
		year = req.POST.get("year")
		price = req.POST.get("price")
		data = (book, year, price)
		cur.execute("INSERT INTO books (book,year,price) VALUES (?,?,?)", data)
		con.commit()

	if req.POST.get("delete"):
		id = req.POST.get("id")
		cur.execute("DELETE FROM books WHERE id = ?" , id)
		con.commit()

	books = cur.execute("SELECT * FROM books").fetchall()
	
	x = {
		"books" : books
	}

	

    




	return render(req, "about.html", x )


def services(r):
	return render(r,"services.html")

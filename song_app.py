from flask import *
import sqlite3 as sql

app  = Flask(__name__)

@app.route('/')
def main():
	#create connection
	conn  = sql.connect('/home/sahajanand/Desktop/Crawlar/song.db')
	#create cursor
	conn.row_factory = sql.Row
	cur = conn.cursor()
	#execute query
	# cur.execute("select * from msong ORDER BY TimeStamp DESC")
	# data = cur.fetchall();

	cur.execute("select Distinct MovieName from ssong ORDER BY TimeStamp DESC LIMIT 20")
	data1 = cur.fetchall();

	return render_template('index.html',data1  = data1)

@app.route('/showsong/<string:mname>')
def showsong(mname):
	conn  = sql.connect('/home/sahajanand/Desktop/Crawlar/song.db')
	#create cursor
	conn.row_factory = sql.Row
	cur = conn.cursor()
	#execute query
	cur.execute("select * from msong where MovieName = ?",[mname])
	mlink = cur.fetchall();	

	cur.execute("select * from ssong where MovieName = ?",[mname])
	slink = cur.fetchall();

	return render_template('links.html',mlink=mlink,slink=slink,mname = mname)


if __name__ == '__main__':
	app.run(debug=True)

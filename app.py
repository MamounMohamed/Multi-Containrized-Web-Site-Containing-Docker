from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)
#the web container seems to run before the database is initialized with init.sql, this handles it
error = True
while error:
	error = False
	try:
		mydb = mysql.connector.connect(
			host='db',
			user='root',
			password='root',
			database="project"
		)
	except mysql.connector.Error as err:
		error = True
cur = mydb.cursor()
def get_ids():
	cur.execute("SELECT student_name, id FROM students")
	ids = cur.fetchall()
	return ids
@app.route("/")
def index():
	ids = get_ids();
	return render_template('index.html', ids=ids)

@app.route("/search", methods=["POST"])
def search():
	key = request.form.get("id")
	query = "SELECT * FROM students WHERE id=" + key
	cur.execute(query)
	student = cur.fetchall()
	ids = get_ids()
	return render_template("card.html", ids=ids, student=student)
if __name__ == '__main__':
	from waitress import serve
	serve(app, host="0.0.0.0")
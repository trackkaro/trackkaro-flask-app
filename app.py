from flask import Flask, render_template, redirect, url_for, request
from passlib.hash import sha256_crypt
import json
import psycopg2 as pg2

'''
def user_dataTable():
	conn=pg2.connect(database='portfolio tracker test',user='postgres', password='password')
	cur=conn.cursor()
	try:

		query="""INSERT INTO USER_CREDENTIAL(FIRST_NAME, LAST_NAME,EMAIL,PASS_WORD,USERNAME)VALUES(%s, %s, %s, %s, %s)"""
		data_to_insert=[('ASHIKA','KETCHUM','ASH69@GMAIL.COM','ASHOCKS','ASH619'),
						('MISTYKA','COCKSUKER','MCS@GMAIL.COM','MISTYSUXX','MISTY619'),
						('BROCKY', 'theBBC','BROCKBBC@GMAIL.COM','BROCKBBCX','BROCK619')]

		cur=conn.cursor()
		cur.executemany(query,data_to_insert)
		conn.commit()
		conn.close
	except Exception as e:
		print(str(e))
'''

app = Flask(__name__,template_folder='templates')

@app.route('/', methods=["GET", "POST"])
def create_account():
	if request.method == "POST":
		print(request.form['firstName'],request.form['lastName'],request.form['userName'],
			request.form['password'],request.form['email'])
		
		 

		conn=pg2.connect(database='portfolio tracker test',user='postgres', password='password')
		cur=conn.cursor()
		try:

			query=f"INSERT INTO USER_CREDENTIALSS(FIRST_NAME, LAST_NAME,EMAIL,PASS_WORD,USERNAME)VALUES('{request.form['firstName']}', '{request.form['lastName']}', '{request.form['email']}', '{sha256_crypt.encrypt(request.form['password'])}', '{request.form['userName']}')"


			cur=conn.cursor()
			cur.execute(query)
			conn.commit()
			conn.close

		except Exception as e:
			return render_template('register.html',message="Registration failed. Please try again. " + str(e))
		return render_template('register.html',message="Registration Sucessful")
	else:
		return render_template('register.html')   






@app.route('/login', methods=["GET","POST"])
def login():

	if request.method == "POST":
		#fetch hash for request.form['email']
		#verify hash with request.form['password']
		#set session variable
		conn=pg2.connect(database='portfolio tracker test',user='postgres', password='password')
		cur=conn.cursor()
		try:
			query1= f"SELECT PASS_WORD FROM USER_CREDENTIALSS WHERE EMAIL = '{request.form['email']}'"
		

			cur=conn.cursor()
			cur.execute(query1)
			data_fetch=cur.fetchall()
			if len(data_fetch)>0:
				#print(data_fetch)
				verified=sha256_crypt.verify(request.form['password'], data_fetch[0][0])
				if verified:
					return render_template('login.html',message="Login Successful.")
				else:
					return render_template('login.html',message="Invalid Email/Password.")


			else:

				return render_template('login.html',message='Please enter a vaild username or password.')
		
		except Exception as e:
			return render_template('login.html',message='error occured')
		conn.close
	
		return render_template('home.html')
	else:
		return render_template('login.html')


'''@app.route('/validate', methods=["POST"])
def validate():
	if request.method=='POST':
		return redirect(url_for('success'))
	return redirect(url_for('login'))
'''

if __name__=='__main__':
	app.run(debug=True)


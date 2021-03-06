from flask import Flask, render_template, request, redirect
from passlib.hash import sha256_crypt
import psycopg2 as pg2
from search import search
from fetch import get_data_yf
from get_tick_data import get_tick_data

app = Flask(__name__, template_folder='templates')
app.secret_key = "9ZSo4tbgZALx4k"


@app.route('/register', methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        print(request.form['firstName'], request.form['lastName'], request.form['userName'],
              request.form['password'], request.form['email'])

        conn = pg2.connect(database='portfolio tracker test',
                           user='postgres', password='password')
        cur = conn.cursor()
        try:

            query = f"INSERT INTO USER_CREDENTIALSS(FIRST_NAME, LAST_NAME,EMAIL,PASS_WORD,USERNAME)VALUES('{request.form['firstName']}', '{request.form['lastName']}', '{request.form['email']}', '{sha256_crypt.encrypt(request.form['password'])}', '{request.form['userName']}')"

            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()

        except Exception as e:
            conn.close()
            return render_template('register.html', message="Registration failed. Please try again. " + str(e))

        return redirect('login.html')
    else:
        return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # fetch hash for request.form['email']
        # verify hash with request.form['password']
        # set session variable
        conn = pg2.connect(database='portfolio tracker test',
                           user='postgres', password='password')
        cur = conn.cursor()
        try:
            query1 = f"SELECT PASS_WORD FROM USER_CREDENTIALSS WHERE EMAIL = '{request.form['email']}'"

            cur = conn.cursor()
            cur.execute(query1)
            data_fetch = cur.fetchall()
            if len(data_fetch) > 0:
                # print(data_fetch)
                verified = sha256_crypt.verify(
                    request.form['password'], data_fetch[0][0])
                conn.close()
                if verified:
                    return redirect('home.html')
                else:
                    return render_template('login.html', message="Invalid Email/Password.")

            else:
                conn.close()
                return render_template('login.html', message='Please enter a vaild username or password.')

        except Exception as e:
            conn.close()
            return render_template('login.html', message='error occured')

    else:
        return render_template('login.html')


@app.route('/search', methods=["GET", "POST"])
def search_page():
    if request.method == "POST":
        search_string = request.form['search_string']
        quotes = search(search_string)

        for i in range(len(quotes)):
            if 'longname' not in quotes[i].keys():
                quotes[i]['longname'] = quotes[i]['shortname']

        # print(quotes)

        return render_template('search.html', quotes=quotes)
    return render_template('search.html')


@app.route('/home', methods=["GET", "POST"])
def home():

    quotes = get_asset('harshit@gmail.com')
    #quotes = [('TSLA', 5), ('MSFT', 5), ('GOOG', 5)]

    if quotes == None:
        return render_template('home.html', message="Add Assets", assets=[])

    tickers = ' '.join([quote[-1] for quote in quotes]).lower()

    datalist = get_data_yf(tickers)

    for i in range(len(datalist)):
        datalist[i]['quantity'] = quotes[i][0]

    return render_template('home.html', assets=datalist)


@app.route('/edit/<ticker>', methods=['GET','POST'])
def edit_page(ticker):
    # fetch ticker details
    if request.method=="GET":
        
        username="harshit@gmail.com"
        print("fetching transactions",username,":",ticker)
        transactions = get_tick_data(username,ticker)
        data = get_data_yf(ticker)[0]
        
        if len(transactions)>0:
            return render_template('edit.html', data=data, transactions=transactions)
            
        else:
            return render_template('edit.html', data=data)
    else:
        return render_template('edit.html', data=data)


@app.route('/logout')
def logout():
    return redirect('/login')


def get_asset(username):
    conn = pg2.connect(database='portfolio tracker test',
                       user='postgres', password='password')
    cur = conn.cursor()
    try:
        query2 = f"select sum(buy_quantity) as total_quantity,buying_data.ticker_id, tick_data.quote_type, tick_data.long_name, tick_data.exchange, tick_data.ticker from buying_data inner join tick_data on buying_data.ticker_id=tick_data.ticker_id where username='{username}' group by buying_data.ticker_id,tick_data.long_name, tick_data.exchange, tick_data.ticker, tick_data.quote_type"
        cur.execute(query2)
        data_fetch = cur.fetchall()
        lst = list(data_fetch)
        conn.close()
        return lst
    except Exception as e:
        print('error')
    conn.close()
    return None


if __name__ == '__main__':
    app.run(debug=True)

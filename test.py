from flask import Flask, render_template
import psycopg2 as pg2
from fetch import get_data_yf

app = Flask(__name__, template_folder='templates')
app.secret_key = "9ZSo4tbgZALx4k"


@app.route('/', methods=["GET", "POST"])
def home():

    #quotes = get_asset('meet@gmail.com')
    quotes = [('TSLA', 5), ('MSFT', 5), ('GOOG', 5)]

    if quotes == None:
        return render_template('home.html', message="Add Assets", assets=[])

    tickers = ' '.join([quote[0] for quote in quotes]).lower()

    datalist = get_data_yf(tickers)

    for i in range(len(datalist)):
        datalist[i]['quantity'] = quotes[i][1]

    return render_template('home.html', assets=datalist)


if __name__ == '__main__':
    app.run(debug=True)

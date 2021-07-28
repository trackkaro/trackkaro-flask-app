import psycopg2 as pg2
from fetch import get_data_yf


def get_tick_data(username,ticker):
	conn=pg2.connect(database='portfolio tracker test',user='postgres',password='password')
	cur=conn.cursor()
	try:
		query3=f"select tick_data.ticker,tick_data.long_name, tick_data.exchange,tick_data.quote_type,tick_data.currency,buying_data.buy_quantity,buying_data.buy_id from buying_data inner join tick_data on buying_data.ticker_id=tick_data.ticker_id where username='meet@gmail.com' and tick_data.ticker='TSLA' group by buying_data.buy_quantity,buying_data.ticker_id,tick_data.ticker_id,tick_data.long_name, tick_data.exchange, tick_data.ticker, tick_data.quote_type,tick_data.currency,buying_data.buy_id"
		cur.execute(query3)
		data_fetch= cur.fetchall()
		lst= list(data_fetch)
		return lst 
	except Exception as e:
		print('error')
	conn.close()
	return None
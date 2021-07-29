import psycopg2 as pg2
from fetch import get_data_yf

def add_tick_data(ticker,long_name,quote_type,exchange):
	conn=pg2.connect(database='portfolio tracker test',user='postgres',password='password')
	cur=conn.cursor()

	try:
		query=f"insert into tick_data(ticker,quote_type,exchange,long_name) values('{ticker}','{quote_type}','{exchange}','{long_name}')"
		q=cur.execute(query)
		conn.commit()
		conn.close()
		
	except Exception as e:
		print('error')
	conn.close()
	return None
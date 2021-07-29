import psycopg2 as pg2
from fetch import get_data_yf

def add_data(ticker_id,username):
	conn=pg2.connect(database='portfolio tracker test',user='postgres',password='password')
	cur=conn.cursor()

	try:
		query=f"insert into buying_data(ticker_id,username,buy_price,buy_quantity) values('{ticker_id}','{username}',0,0)"
		cur.execute(query)
		conn.commit()
		conn.close()
		
		
	except Exception as e:
		print('error')
	conn.close()
	return None
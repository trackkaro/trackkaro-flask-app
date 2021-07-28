import psycopg2 as pg2
from fetch import get_data_yf


def edit_data(buy_price,buy_quantity):
	conn=pg2.connect(database='portfolio tracker test',user='postgres',password='password')
	cur=conn.cursor()
	try:
		query=f"update buying_data set buy_price={buy_price}, buy_quantity={buy_quantity} where ticker_id=545 and username='meet@gmail.com'and buy_id=25;"
		cur.execute(query)
		conn.commit()
		conn.close()
		
		
	except Exception as e:
		print('error')
	conn.close()
	return None
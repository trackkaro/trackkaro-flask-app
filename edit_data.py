import psycopg2 as pg2
from fetch import get_data_yf


def edit_data(buy_price,buy_quantity,ticker_id,username,buy_id):
	conn=pg2.connect(database='portfolio tracker test',user='postgres',password='password')
	cur=conn.cursor()
	try:
		query=f"update buying_data set buy_price={buy_price}, buy_quantity={buy_quantity} where ticker_id={ticker_id} and username='{username}' and buy_id='{buy_id}';"
		cur.execute(query)
		conn.commit()
		conn.close()
		
		
	except Exception as e:
		print('error' +str(e))
	conn.close()
	return None
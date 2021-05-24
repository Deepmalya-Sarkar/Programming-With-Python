import psycopg2 as pg2
conn=pg2.connect(database='dvdrental',user='postgres', password='password')
cur=conn.cursor()
cur.execute('SELECT * FROM payment')
data=cur.fetchone()
print(data)
conn.close()
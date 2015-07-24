import sqlite3 as lite
con = lite.connect('getting_started.db')
with con:
  cur = con.cursor()
  #cur.execute('SELECT name, state, year, warm_month, cold_month, average_high FROM cities INNER JOIN weather ON name = city');
  cur.execute('SELECT state, average_high FROM cities INNER JOIN weather ON name = city GROUP BY state');
  rows = cur.fetchall()
  for row in rows:
    print row

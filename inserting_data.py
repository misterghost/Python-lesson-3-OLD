import sqlite3 as lite
con = lite.connect('getting_started.db')
with con:
  cur = con.cursor()
  cur.execute("INSERT INTO cities VALUES('Monterrey', 'NL', 'Mex')")
  cur.execute("INSERT INTO cities VALUES('Torreon', 'CO', 'USA')")
  cur.execute("INSERT INTO cities VALUES('Savannah', 'GA', 'USA')")
  cur.execute("INSERT INTO weather VALUES('Monterrey', 2013, 'July', 'January', 12)")
  cur.execute("INSERT INTO weather VALUES('Torreon', 2013, 'July', 'January', 39)")
  cur.execute("INSERT INTO weather VALUES('Savannah', 2013, 'June', 'February', 71)")
  print('done')

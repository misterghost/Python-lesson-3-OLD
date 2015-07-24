import sqlite3 as lite
cities = (('Las Vegas', 'NV', 'USA'), ('Atlanta', 'GA', 'USA'), ('Culiacan', 'SI', "ME"))
weather = (('Las Vegas', 2013, 'July', 'December', 45), ('Atlanta', 2013, 'May', 'March', 33), ('Culiacan', 2013, 'April', 'June', 55))
con = lite.connect('getting_started.db')
with con:
  cur = con.cursor()
  cur.executemany("INSERT INTO cities VALUES(?,?,?)", cities)
  cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
print('its done')
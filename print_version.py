import sqlite3 as lite

cities = (('Las Vegas', 'NV', 'tri'),
                    ('Atlanta', 'GA', 'duo'))
weather = (('Las Vegas', 2013, 'July', 'December', 55),
                      ('Atlanta', '2013', 'July', 'January', 55))

con = lite.connect('getting_started.db')

with con:
  cur = con.cursor() 
  cur.executemany("INSERT INTO cities VALUES(?,?,?)", cities)
  cur.executemany("INSERT INTO weather Values(?,?,?,?,?)", weather)   
  #cur.execute("INSERT INTO cities VALUES('Washington', 'DC', 'tri')")
  #cur.execute("INSERT INTO cities VALUES('Houston', 'TX', 'due')")
  #cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', '53')")
  #cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', '55')")

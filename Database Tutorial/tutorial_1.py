import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS plottingtable(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO plottingtable VALUES(140895, '2018-04-05','Python', 19 )")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value= random.randrange(0,10)
    c.execute("INSERT INTO plottingtable(unix, datestamp, keyword, value) VALUES(?,?,?,?)",
              (unix, date, keyword,value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM plottingtable ')#to read from database
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row[0])



#create_table()
#data_entry()
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)
c.close()
conn.close()


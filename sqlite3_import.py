import sqlite3
from customer_points import Customer
from faker import Faker

#stores file and creates in-memory database
conn = sqlite3.connect('customer_points.db')

c = conn.cursor()

#c.execute("""CREATE  TABLE customers (
#                first text,
#                last text,
#                points intger
#                )""")
cust_1 = Customer(fake.name, fake.seed)
cust_2= Customer('Holly ', 'Burns', 12039)


 
c.execute("Insert INTO customers VALUES (?,?,?)",(cust_1.first,cust_1.last,cust_1.points))
conn.commit()

 

c.execute("SELECT * FROM customers WHERE last = 'Smith'")

print(c.fetchall())
conn.commit()
conn.close()

# Databases

import sqlite3

class Stocks:
    def __init__(self, name, quantity, price, invest):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.invest = invest

# Inserting values
def insert_stocks(stock):
    with conn: # with conn: is used so that we don't have to commit() everytime
        c.execute("INSERT INTO Stocks VALUES (:name, :quantity, :price, :invest)",
                  {'name': stock.name, 'quantity': stock.quantity, 'price': stock.price, 'invest': stock.invest})

conn = sqlite3.connect('miniproject.db') # Connect to Database stored in RAM
c = conn.cursor() # Creating a cursor to execute SQL Commands

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS Stocks (
            name text,
            quantity integer,
            price real,
            invest real
        )""")

#with conn:
#    c.execute("CREATE VIEW IF NOT EXISTS Port as SELECT name, SUM(quantity) as quantity, AVG(price) as price, SUM(invest) as invest FROM Stocks GROUP BY name")

import sqlite3
from Customer import Customer

# DAO - Data Access Object
class CustomerDataAccess:

    def __init__(self, file_path):
        self.con = sqlite3.connect(file_path)
        self.cursor = self.con.cursor()

    def print_all_customers(self):
        self.cursor.execute("select * from customer")
        for row in self.cursor:
            print(row)

    def insert_customer(self, customer):
        self.cursor.execute(f'INSERT INTO customer VALUES ("{customer.id}", ' +
                    f' "{customer.fname}", "{customer.lname}",' +
                    f' "{customer.mobile}", "{customer.address}")')
        self.con.commit()

    def get_customer_by_id(self, id):
        self.cursor.execute("select * from customer where "+
                         f" id = {id}")
        customer = None
        for row in self.cursor:
            customer = Customer(row[0], row[1], row[2], row[3], row[4])
        return customer

    def delete_customer(self, id):
        self.cursor.execute("delete from customer where " +
                            f" id = {id}")
        self.con.commit()

    def update_customer(self, id, customer):
        self.cursor.execute(f'UPDATE customer SET  id = {customer.id}, ' +
                            f' fname = "{customer.fname}", lname = "{customer.lname}",' +
                            f' mobile = "{customer.mobile}", address = "{customer.address}" where id = {id} ' )
        self.con.commit()

db = r'C:\sqlite\customer.db'
a = CustomerDataAccess(db)
b = Customer(9, 'Bell', 'Harw', 'California', 6576)

#print(a.insert_customer(b))
#print(a.get_customer_by_id(2))
#print(a.delete_customer(3))
#print(a.update_customer(4,b))
#print(a.print_all_customers())
#rint(a.update_customer(4,b))
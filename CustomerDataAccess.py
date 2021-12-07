import sqlite3
from Customer import Customer

# DAO - Data Access Object
class CustomerDataAccess:

    def __init__(self, file_path):
        con = sqlite3.connect(file_path)
        self.cursor = con.cursor()

    def print_all_customers(self):
        self.cursor.execute("select * from customer")
        for row in self.cursor:
            print(row)

    def insert_customer(self, customer):
        self.cursor.execute(f'INSERT INTO customer VALUES ({customer.id}, ' +
                    f' "{customer.fname}", "{customer.lname}",' +
                    f' "{customer.mobile}, {customer.address}")')

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

    def update_customer(self, id, customer):
        self.cursor.execute(f'UPDATE customer SET ({customer.id}, ' +
                            f' "{customer.fname}", "{customer.lname}",' +
                            f' "{customer.mobile}, {customer.address}") where id = {id}')

db = r'C:\sqlite\customer.db'
a = CustomerDataAccess(db)

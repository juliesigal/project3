import sqlite3
from Customer import Customer
from CustomerDataAccess import CustomerDataAccess

# dao = CustomerDataAccess('mydb.db')
# dao.print_all_customers();

db = r'C:\sqlite\customer.db'
a = CustomerDataAccess(db)
b = Customer()

print('Please enter you choice:' + \
      '1. Get all customers' +
      '2. Get customer by id' +
      '3.  Insert customer' +
      '4. Delete customer' +
      '5. Update customer' +
      '6. Exit')

choise = int(input('please enter your choise: '))
if choise == 1:
    print(a.print_all_customers())
elif choise == 2:
    print(a.get_customer_by_id(1))
elif choise == 3:
    print(a.insert_customer(b))
elif choise == 4:
    print(a.delete_customer(1))
else:
    print(a.update_customer(1,b))

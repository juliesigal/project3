class Customer:
    def __init__(self, id, fname, lname, address, mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile = mobile

    def __str__(self):
        return f'id = {self.id}, first name is {self.fname}, last name is {self.lname}' +\
        f'then adress is {self.address} and mobile number is {self.mobile}'

    def __repr__(self):
        return f'id = {self.id}, first name is {self.fname}, last name is {self.lname}' + \
               f'then adress is {self.address} and mobile number is {self.mobile}'
from sqlconnector import mydb


class Old_People(object):
    insert_user = mydb.cursor(buffered=True)

    def __init__(self, Id, firstname, lastname, email, dob, about, address, idproof, money, contact_no, notify, password):
        self.id = Id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.dob = dob
        self.about = about
        self.address = address
        self.idproof = idproof
        self.money = money
        self.contact_no = contact_no
        self.notify = notify
        self.password = password
    def get_details(self):
        print("Name: ",self.firstname,self.lastname)
        print("Email: ",self.email)
        print("Contact No.: ",self.contact_no)

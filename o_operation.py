# performs various operation on the old_people table

from sqlconnector import mydb
from old_people import Old_People

class o_operation(object):
    o_user = mydb.cursor(buffered=True)

    # function to show all users
    def show_all(self):
        sql = "select * from old_people"
        self.o_user.execute(sql)
        myresult = self.o_user.fetchall()
        for x in myresult:
            print(x)
        
    #function to insert a new user
    def insert(self,firstname,lastname,email,dob,about,address,idproof,money,contact_no,password):
        sql = "insert into old_people(firstname,lastname,email,dob,about,address,idproof,money,contact_no,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (firstname, lastname, email, dob,
               about, address, idproof,money,contact_no,password)
        self.o_user.execute(sql, val)
        mydb.commit()
        x=self.o_user.lastrowid
        return Old_People(x,firstname,lastname,email,dob,about,address,idproof,money,contact_no,None,password)

    # function to show details about a user
    def show_user(self, email,password):
        sql = 'select * from old_people where email=%s and password=%s'
        val = (email,password)
        self.o_user.execute(sql, val)
        myresult = self.o_user.fetchone()
        return Old_People(myresult[0],myresult[1],myresult[2],myresult[3],myresult[4],myresult[5],myresult[6],myresult[7],myresult[8],myresult[9],myresult[10],myresult[11])

    # function to show reviews of a user
    def show_review_user(self, ID):
        sql = 'select * from review_old where o_id=%s'
        val = (ID,)
        self.o_user.execute(sql, val)
        myresult = self.o_user.fetchall()
        for x in myresult:
            print(x)

    # function to add review of user
    def add_review_user(self,review,rating,o_id,y_id):
        sql="insert into review_old(review,rating,o_id,y_id) values(%s,%s,%s,%s)"
        val=(review,rating,o_id,y_id)
        self.o_user.execute(sql, val)
        mydb.commit()
        return self.o_user.lastrowid

    # function to approve a young chap for care
    def approve_for_care(self,y_id,o_id):
        sql="update old_people set care_taken=%s where id=%s"
        val=(y_id,o_id)
        self.o_user.execute(sql, val)
        mydb.commit()

        sql="insert into young_old (y_id,o_id) values(%s,%s)"
        val=(y_id,o_id)
        self.o_user.execute(sql, val)
        mydb.commit()
        
        #notify young person
        sql = 'select firstname,lastname,email,contact_no from old_people where id=%s'
        val = (o_id,)
        self.o_user.execute(sql, val)
        myresult = self.o_user.fetchone()
        string="You have been approved for care by "+myresult[0]+" "+myresult[1]+". Person email: "+myresult[2]+" ,Contact No."+myresult[3]
        sql="update young_people set notify=%s where id=%s"
        val=(string,y_id)
        self.o_user.execute(sql, val)
        mydb.commit()
        
        #Clear all entry of old people who has been requested for approval in the approval_applied table
        sql="delete from approval_applied where o_id=%s"
        val=(o_id,)
        self.o_user.execute(sql, val)
        mydb.commit()

    # function to show young_people who have requested for care of the older couple
    def applied_care(self,o_id):
        sql = 'select * from young_people where id in (select y_id from approval_applied where o_id=%s)'
        val=(o_id,)
        self.o_user.execute(sql, val)
        myresult = self.o_user.fetchall()
        for x in myresult:
            print(x)

    #function to show previous young_people who has taken care of older couple
    def show_previous_people(self,o_id):
        sql = 'select * from young_people where id in (select y_id from young_old where o_id=%s)'
        val=(o_id,)
        self.o_user.execute(sql, val)
        myresult = self.o_user.fetchall()
        for x in myresult:
            print(x)

    # function to show who is taking care of the older couple
    def show_care(self, ID):
        sql = 'select * from young_people where id=(select care_taken from old_people where id=%s)'
        val = (ID,)
        self.o_user.execute(sql, val)
        myresult = self.o_user.fetchall()
        for x in myresult:
            print(x)
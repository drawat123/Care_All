# performs various operation on the young_people table

from sqlconnector import mydb
from young_people import Young_People

class y_operation(object):
    y_user = mydb.cursor(buffered=True)

    # function to show all users
    def show_all(self):
        sql = "select * from young_people"
        self.y_user.execute(sql)
        myresult = self.y_user.fetchall()
        for x in myresult:
            print(x)
        
    #function to insert a new user
    def insert(self,firstname,lastname,email,dob,about,address,idproof,contact_no,password):
        sql = "insert into young_people(firstname,lastname,email,dob,about,address,idproof,contact_no,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (firstname, lastname, email, dob,
               about, address, idproof, contact_no,password)
        self.y_user.execute(sql, val)
        mydb.commit()
        x=self.y_user.lastrowid
        return Young_People(x,firstname,lastname,email,dob,about,address,idproof,contact_no,None,password)

    # function to show details about a user
    def show_user(self, email,password):
        sql = 'select * from young_people where email=%s and password=%s'
        val = (email,password)
        self.y_user.execute(sql, val)
        myresult = self.y_user.fetchone()
        return Young_People(myresult[0],myresult[1],myresult[2],myresult[3],myresult[4],myresult[5],myresult[6],myresult[7],myresult[8],myresult[9],myresult[10])

    # function to show reviews of a user
    def show_review_user(self, ID):
        sql = 'select * from review_young where y_id=%s'
        val = (ID,)
        self.y_user.execute(sql, val)
        myresult = self.y_user.fetchall()
        for x in myresult:
            print(x)

    # function to add review of user
    def add_review_user(self,review,rating,y_id,o_id):
        sql="insert into review_young(review,rating,y_id,o_id) values(%s,%s,%s,%s)"
        val=(review,rating,y_id,o_id)
        self.y_user.execute(sql, val)
        mydb.commit()
        return self.y_user.lastrowid

    # function to apply for care of old people
    def apply_for_care(self,y_id,o_id):
        sql="select count(id) from approval_applied where y_id=%s and o_id=%s"
        val=(y_id,o_id)
        self.y_user.execute(sql, val)
        myresult = self.y_user.fetchone()
        if myresult[0] != 0:
            print("Already applied")
            return
        
        sql="select count(id) from old_people where care_taken=%s"
        val=(y_id,)
        self.y_user.execute(sql, val)
        myresult = self.y_user.fetchone()
        if myresult[0]<4:
            sql="insert into approval_applied(y_id,o_id) values(%s,%s)"
            val=(y_id,o_id)
            self.y_user.execute(sql, val)
            mydb.commit()
            return self.y_user.lastrowid
        else:
            print("Already taking care of 4 people")

    # function to show old people who are requested for approval of their care by the young chap
    def applied_care(self,y_id):
        sql = 'select * from old_people where id in (select o_id from approval_applied where y_id=%s)'
        val=(y_id,)
        self.y_user.execute(sql, val)
        myresult = self.y_user.fetchall()
        for x in myresult:
            print(x)

    #function to show previous old people the young chap has taken care of
    def show_previous_people(self,y_id):
        sql = 'select * from old_people where id in (select o_id from young_old where y_id=%s)'
        val=(y_id,)
        self.y_user.execute(sql, val)
        myresult = self.y_user.fetchall()
        for x in myresult:
            print(x)

    # function to show who all a young chap is currently taking taking care of
    def show_care(self, ID):
        sql = 'select * from old_people where care_taken=%s'
        val = (ID,)
        self.y_user.execute(sql, val)
        myresult = self.y_user.fetchall()
        for x in myresult:
            print(x)

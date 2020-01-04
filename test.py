from young_people import Young_People
from y_operation import y_operation
from old_people import Old_People
from o_operation import o_operation

y_op = y_operation()
o_op = o_operation()

print("Function to show who all a young chap is taking care of")
y_op.show_care(4)
print()
print("Function to show who is taking care of the old person")
o_op.show_care(5)
print()
print("Function to show review of the young person")
y_op.show_review_user(4)
print()
print("Function to show review of the old person")
o_op.show_review_user(7)
print()
print("Function to show detail of the young person")
x=y_op.show_user("ajay@gmail.com",1234)
x.get_details()
print()
print("Function to show detail of the old person")
x=o_op.show_user("r@outlook.com",1234)
x.get_details()


print()
print("All young people")
y_op.show_all()
print()
print("All old people")
o_op.show_all()

#x=y_op.insert("abc","def","abc@gmail.com","1997-05-22","Student","Delhi","771922224567","9811111111","1234")
#x=o_op.insert('xyz', 'wxd', 'xyz@gmail.com', "1955-4-13", 'Retired employee', 'Bengaluru', '680012345678', 5120, '9887891234', '1234')
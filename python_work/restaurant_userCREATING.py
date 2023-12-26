# Importing a certain file and checking if it is importing by calling methods!
from cars import Restaurant

my_restaurant = Restaurant('Chick-Fil-A', 'chicken sandwiches')
my_restaurant.describe_restaurant()



# Importing another certain file and checking if it is importing by calling methods! (This time applying inheritence)
from cars import Admin, Privileges, User

admin = Admin('Justin', 'Champ', 41, 'Male', 69, 153)
admin_privilege = Privileges(["can add post", "can delete post", "can ban user", "can add user", "can see user's info/records", "can track user", "can fire user", "can direct user", "can call user", "can schedule almost anything"])
user = User('Anish', 'Pasumarthi', 13, 'Male', 65, 98)

# Showing privileges as an admin
admin.privilege.show_privileges()



"""
I already stored the User class in one module, and store the Privileges and Admin classes in a separate module. 
In a separate file, created an Admin instance and call show_privileges() to show that everything is still working correctly.
"""
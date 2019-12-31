from userclass import Users

class Privileges():

    def __init__(self, access=[]):

        self.access = access
    
    def show_privileges(self):
        print("The admin has the following privileges: " + str(self.access))


class Admin(Users):
    def __init__(self, first_name, last_name, job_title, dept, login, login_attempts):
        super().__init__(first_name, last_name, job_title, dept, login, login_attempts)
        self.privileges = Privileges()
class Users():
    
    def __init__(self, first_name, last_name, job_title, dept, login, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.dept = dept
        self.login = login
        self.login_attempts = 0
    
    def describe_user(self):
        print("\nThe user's name is " + self.first_name + " " + self.last_name + "." "\nThe job title is " + self.job_title + " in the " 
        + self.dept + " department." "\nThe login is " + self.login + ".")
    
    def greet_user(self):
        print("\nWelcome " + self.first_name + " " + self.last_name + ". Please read the terms of use for company assets. All usage will be monitored and violations of terms of use can lead to discipline up to and including termination. Thank you.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



mulroneyb = Users("Brian", "Mulroney", "Prime Minister", "Canadian Federal Government", "mulroneyb", 0)
torresjc = Users("JC", "Torres", "Short Order Cook", "Kitchen", "torresjc", 0)
singhg = Users("Gursharan", "Singh", "Graduate Student", "School of Business", "singhg", 0)
fricanoa = Users("Anthony", "Fricano", "Stock Room Team Lead", "Stock Room", "fricanoa", 0)
ferreraa = Users("Andy", "Ferrera", "Independent Broker", "Insurance Agency", "ferreraa", 0)

mulroneyb.describe_user()
mulroneyb.greet_user()
torresjc.describe_user()
torresjc.greet_user()
singhg.describe_user()
singhg.greet_user()
fricanoa.describe_user()
fricanoa.greet_user()
ferreraa.describe_user()
ferreraa.greet_user()

singhg.increment_login_attempts()
singhg.increment_login_attempts()
singhg.increment_login_attempts()

print("The user " + singhg.login + ", has " + str(singhg.login_attempts) + " incorrect logins.")

singhg.reset_login_attempts()

print("The user " + singhg.login + ", has " + str(singhg.login_attempts) + " incorrect logins.")

class Privileges():

    def __init__(self, privileges=[]):

        self.privileges = privileges  
    
    def show_privileges(self):
        print("The admin has the following privileges: " + str(self.privileges))

class Admin(Users):
    def __init__(self, first_name, last_name, job_title, dept, login, login_attempts):
        super().__init__(first_name, last_name, job_title, dept, login, login_attempts)
        self.privileges = Privileges()



SuperUser = Admin('Marc', 'Freiman', 'Desktop Support', 'MIS', '!freimanm', 0)

SuperUser.privileges.privileges = ['add user', 'delete user', 'change group memberships', 'unlock', 'reset']

SuperUser.privileges.show_privileges()




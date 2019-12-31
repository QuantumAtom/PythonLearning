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

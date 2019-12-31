class Employees():
    """Employee and salary information"""
    def __init__(self, FName, LName, Salary):
        """Store the employee's name and salary"""
        self.FName = FName
        self.LName = LName
        self.Salary = Salary

    
    def give_raise(self, payincrease=5000):
        """Raise for Employee"""
        self.Salary += payincrease

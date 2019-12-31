class Restaurant():

    """This class is presumably for restaurants"""
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 
        self.number_served = 100
        
    def describe_restaruant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The chef prepares " + self.cuisine_type + " cuisine.")
        
    def open_restaurant(self):
        print(self.restaurant_name + " is now open for diners.")

    def set_number_served(self, serviced):
        self.number_served = serviced
    
    def increment_number_served(self, servedincrease):
        self.number_served += servedincrease

class IceCreamStand(Restaurant):
    """Initializing subclass IceCreamStand"""
    def __init__(self, restaurant_name, cuisine_type, number_served):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavor = []
    
    def display_flavors_list(self):
        print("Here are the list of flavors: " + str(self.flavor))



#IVillage = Restaurant('Italian Village', 'Italian')

#IVillage.describe_restaruant()

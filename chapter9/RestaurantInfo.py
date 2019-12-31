from restaurants import Restaurant

EggHarbor = Restaurant('Egg Harbor Cafe', 'Breakfast', 0)

EggHarbor.describe_restaruant()

EggHarbor.set_number_served(200)

EggHarbor.increment_number_served(50)

print("This restaurant serves " + str(EggHarbor.number_served) + " patrons.")

#BerryYo = IceCreamStand('BerryYo', 'Yogurt', 0)

#BerryYo.flavor = ['Chocolate', 'Vanilla', 'Caramel', 'Peanut Butter', 'Chocolate Chip Cookie Dough', 'French Vanilla']

#BerryYo.display_flavors_list()
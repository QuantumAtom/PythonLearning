favorite_fruits = ["Apples", "Bananas", "Grapes"]

served = []

if "Pineapples" in favorite_fruits:
    served.append("pineapples")
if "Apples" in favorite_fruits:
    served.append("apples")
if "Mangos" in favorite_fruits:
    served.append("mangos")
if "Grapes" in favorite_fruits:
    served.append("grapes")

for food in served:
    print("Please serve " + food + ".")
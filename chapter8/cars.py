def cars(manufacturer, model, **features):
    auto = {}
    auto['manufacturer'] = manufacturer
    auto['model'] = model
    for key, value in features.items():
        auto[key] = value
    return auto

manufacturer = input("Who is the manufacturer?: ")
model = input("What is the model?: ")
more_info = True
while more_info:
    infotype = input("What type of information do you want to enter?: ")
    information = input("What information do you want to enter?: ")
    yes_more = input("Do you have a more information to enter? (Y or N)")
    if yes_more == "Y":
        more_info = True
    else:
        more_info = False

#TempAuto = cars(manufacturer, model, **infotype=information)
TempAuto = cars(manufacturer="chevy",model="malibu", year="2010", transmission="automatic")
auto = {}
auto.update(TempAuto)
print(auto)
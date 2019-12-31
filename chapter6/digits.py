famous = {
    'Bill Gates':{
        '1st': "Microsoft",
        '2nd': "Bill and Melinda Gates Foundation",
        '3rd': "giving away wealth",
    },
    
    'Sergey Brin':{
        '1st': "Google",
        '2nd': "Alphabet",
        '3rd': "being a Russian Jewish refugee",
    },   
    
    'Warren Buffet':{ 
        '1st': "Berkshire Hathaway",
        '2nd': "being extremely wealth",
        '3rd': "being a wealthy Democrat",
    },

    'Paul McCartney':{ 
        '1st': "the Beatles",
        '2nd': "vegetarian",
        '3rd': "Wings",
    },    
        
    'Yitzhak Rabin': {
        '1st': "founding of the State of Israel",
        '2nd': "Oslo Accords",
        '3rd': "assassination",
    },

}

for names, order in famous.items():
    uno = order['1st']
    dos = order['2nd']
    tres = order['3rd']
    print("\n" + names + " is famous for " + str(uno) + ".")
    print(names + " is also famous for " + str(dos) + ".")
    print(names + " is finally famous for " + str(tres) + ".")


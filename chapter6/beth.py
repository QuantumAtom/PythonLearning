family = {

    'beth': {
        'vocation': 'lawyer',
        'employer': 'Apt Electronics',
        'spouse': 'jack',
        'children': 'Alex, Hedy, and Hannah',
    },

    'brian': {
        'vocation': 'lawyer',
        'employer': 'Brian Freiman, Attorney At Law',
        'spouse': 'becky',
        'children': 'none',
    },

    'allan': { 
        'vocation': 'landlord',
        'employer': 'Freiman Properties',
        'spouse': 'Hedy Freiman',
        'children': 'Marc, Brian, and Beth',
    },

    'jack': {
        'vocation': 'lawyer',
        'employer': 'unsure',
        'spouse': 'beth',
        'children': ['Alex', 'Hedy', 'Hannah',]
    },

    'becky': {
        'vocation': 'music therapist',
        'employer': 'Greater Chicago Music Therapy',
        'spouse': 'brian',
        'children': 'none',
    },
}

for name, identity in family.items():
    print("\nName: " + name)
    print("Job: " + identity['vocation'])
    print("Employer: " + identity['employer'])
    print("Spouse: " + identity['spouse'])
    print("children")
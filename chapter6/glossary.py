from collections import OrderedDict

defintions = OrderedDict()

defintions = {
    'variable': 'a non-fixed unit that can hold a value',
    'array': 'a list of variables set as one unit',
    'list': 'similar to an array',
    'condition': 'something that has to set before something can happen',
    'expression': 'kind of like a sentance that can execute something',
    'argument': 'the actual variable or fixed unit that is used in the expression',
    }

for terms, meaning in defintions.items():
    print (terms + ": " + meaning)
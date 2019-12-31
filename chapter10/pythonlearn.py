iLearn = 'text_files/learning_python.txt'

with open(iLearn) as pyLearn:
        #for statements in pyLearn:
            #print(statements)
        learning = pyLearn.readlines()

PythonIs = ''       

for learned in learning:
    PythonIs += learned
    

print(PythonIs)

JavaScriptIs = PythonIs.replace('Python', 'JavaScript')

print(JavaScriptIs)


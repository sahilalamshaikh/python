 # letter ='''dear <name>
#           you are selected
#                   <date>''' coustimize it
Letter = ''' Dear <|name|>,
You are selected
date : <|date|>'''

name = input("\n")
date = input("\n")
Letter = Letter.replace("<|name|>",name)
Letter= Letter.replace("<|date|>",date)
print(Letter)
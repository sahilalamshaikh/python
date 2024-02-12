myDict = {
    "Fast": "In a Quik Manner",
    "Harry":"A Coder",
    "Marks": [1,2,5],
    "anotherdict":{'Harry':'Player'}
    }
myDict['Fast']
print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['Marks'])
print(myDict['anotherdict']['Harry'])
# Dictionary methods
print(list(myDict.keys()))#prints the keys of dictionary
print(myDict.values())#prints the keys of dictionary
print(myDict.items())#prints the (keys,values) for all the contents of dictionary
print(myDict)
updateDict = {"Lovish" : "Freind",
              "Harry":"A Dancer"}
myDict.update(updateDict)#updates the dictionary by adding key.value pairs from updateDict
print(myDict)
print(myDict.get("Harry"))# prints value associated with key Harry
print(myDict["harry"])#throws an error as harry2 is not preseent in the dictionary

# the difference between .get and [] sytax in Dictionaries?
print(myDict.get("Harry"))#return none as harry2 is not preseent in the dictionary
print(myDict["harry2"])#throws an error as harry2 is not preseent in the dictionary

# write a program to create a dictionary of hindi words with values as their
# english translation Provide user with an option to look it up
myDict = {"Pankha": "Fan", "Dabba": "Box", "Vastu": "Item"}
print("options are ", myDict.keys())
a = input("Enter the Hindi Word \n")
# print("The meaning of your word is \n",myDict[a])
# print("The meaning of your word is \n",myDict[a])
# below line will not throw an error if the key is not present in
# the dictionary
print("The meaning of your word is \n", myDict.get(a))

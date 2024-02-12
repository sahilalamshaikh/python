#write a program to accept marks of six student in a sorted list 
m1 = int(input("enter Marks for students number 1: ")) 
m2 = int(input("enter Marks for students number 2: "))
m3 = int(input("enter Marks for students number 3: "))
m4 = int(input("enter Marks for students number 4: "))
m5 = int(input("enter Marks for students number 5: "))
m6 = int(input("enter Marks for students number 6: ")) 
myList = [m1,m2 ,m3 ,m4 ,m5 ,m6]
myList.sort()
print(myList)
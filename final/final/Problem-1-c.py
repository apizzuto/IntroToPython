'''
TITLE: Final Exam Question 1c
AUTHOR: Alex Pizzuto
DATE: 5/1/17
DESCRIPTION: Numbered Lists

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 5/1/17

'''

num = int(input("How many items do you want to enter? "))
myList = []
for item in range(num):
    newThing = input("Enter an item: ")
    myList.append(newThing)
i = 1
for item in myList:
    print("{0}: {1}".format(i,item))
    i = i+1

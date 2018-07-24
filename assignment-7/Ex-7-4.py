'''
TITLE: Ex-7-4
AUTHOR: Alex Pizzuto
DATE: 3/22/17
DESCRIPTION: Accumulation Loops using Lists

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/22/17

'''
def timesTen(myList):
    newList=list()
    for i in range(len(myList)):
        newList.append(10*myList[i])
    return newList

def numbersToStrings(myList):
    newList=list()
    for i in range(len(myList)):
        newList.append(str(myList[i]))
    return newList

print("timesTen applied to [1,2,3,4,5] returns {}.".format(timesTen([1,2,3,4,5])))
print("timesTen applied to [4,7,25,73] returns {}.".format(timesTen([4,7,25,73])))
print("numbersToStrings applied to [1,2,3,4,5] returns {}.".format(numbersToStrings([1,2,3,4,5])))
print("numbersToStrings applied to [4,7,25,73] returns {}.".format(numbersToStrings([4,7,25,73])))

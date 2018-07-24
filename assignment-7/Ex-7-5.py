'''
TITLE: Ex-7-5
AUTHOR: Alex Pizzuto
DATE: 3/22/17
DESCRIPTION: CopyList and revList

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/22/17

'''
def copyList(myList):
    newList=list()
    for i in range(len(myList)):
        newList.append(myList[i])
    return newList

def revList(myList):
    newList=list()
    for i in range(len(myList)):
        newList.insert(0,myList[i])
    return newList

print("copyList applied to [1, 2, 3, 4, 5] returns {}.".format(copyList([1, 2, 3, 4, 5])))
print("copyList applied to [4, 7, 25, 73] returns {}.".format(copyList([4,7,25,73])))
print("revList applied to [1, 2, 3, 4, 5] returns {}.".format(revList([1, 2, 3, 4, 5])))
print("revList applied to [4, 7, 25, 73] returns {}.".format(revList([4, 7, 25, 73])))



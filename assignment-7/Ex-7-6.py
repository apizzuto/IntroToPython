'''
TITLE: Ex-7-6
AUTHOR: Alex Pizzuto
DATE: 3/22/17
DESCRIPTION: Interleaved list function

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/22/17

'''
def zip(myList1, myList2):
    if len(myList1) != len(myList2):
        return list()
    else:
        newList = list()
        for i in range(len(myList1)):
            newList.append(myList1[i])
            newList.append(myList2[i])
            i += 1
        return newList
print('zip(["a","b","c","d"],["e","f","g","h"]) returns {}.'.format(zip(["a","b","c","d"],["e","f","g","h"])))
print('zip(["bill","ted"],["hi","bye"]) returns {}.'.format(zip(["bill","ted"],["hi","bye"])))
print('zip(["hi","professor"],["there","tuckey"]) returns {}.'.format(zip(["hi","professor"],["there","tuckey"])))
print('zip([1,2,3,4],["a","b","c","d"]) returns {}.'.format(zip([1,2,3,4],["a","b","c","d"])))


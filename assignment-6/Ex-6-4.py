'''
TITLE: Ex-6-4
AUTHOR: Alex Pizzuto
DATE: 3/05/17
DESCRIPTION: numberListToString and rangeString defined and tested

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/05/17

'''
def numberListToString(numList):
    myString = ''
    for num in numList:
        myString = myString + str(num) + ' '
    return myString.strip()

def rangeString(start, stopBefore, step):
    myString = numberListToString(range(start,stopBefore,step))
    return myString

print('numberListToString([2,3,4,5,6,7]) returns '+numberListToString([2,3,4,5,6,7]))
print('numberListToString([1,3,5,7,9,11,21,31]) returns '+numberListToString([1,3,5,7,9,11,21,31]))
print('numberListToString([2,4,6,2,5,4,8]) returns '+numberListToString([2,4,6,2,5,4,8]))
print('rangeString(5,20,2) returns '+rangeString(5,20,2))
print('rangeString(1,51,5) returns '+rangeString(1,51,5))
print('rangeString(2,100,10) returns '+rangeString(2,100,10))

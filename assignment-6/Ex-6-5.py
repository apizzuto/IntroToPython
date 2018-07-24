'''
TITLE: Ex-6-5
AUTHOR: Alex Pizzuto
DATE: 3/05/17
DESCRIPTION: factorial exercise

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/05/17


Test cases:
>>> factorial(5)
120
>>> factorial(24)
620448401733239439360000
>>> factorial(6)
720
>>> factorial(52)
80658175170943878571660636856403766975289505440883277824000000000000
'''
def numberListToString(numList):
    myString = ''
    for num in numList:
        myString = myString + str(num) + ' '
    return myString.strip()

def rangeString(start, stopBefore, step):
    myString = numberListToString(range(start,stopBefore,step))
    return myString

def factorial(n):
	fact = 1
	for num in range(1,n+1):
		fact = fact*num
	return fact

num = int(input("Factorial fun! Enter an integer: "))
myString = " * ".join(rangeString(num,0,-1).split())
print(myString + " = "+str(factorial(num)))

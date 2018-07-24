'''
TITLE: Ex-4-4
AUTHOR: Alex Pizzuto
DATE: 2/8/17
DESCRIPTION: Defines functions to return sums of integers from 1 to argument
and sums of squares of numbers from 1 to argument

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/8/17

'''

def sumOfInts(x):
    """Compute the sum of all of the integers from 1 to x"""
    summed=0
    for i in range(x+1):
        summed=summed+i
    return summed

def sumOfSquares(x):
    """Compute the sum of all of the squares of the integers from 1 to x"""
    summed=0
    for i in range(x+1):
        summed=summed+i**2
    return summed


def main():
    num = 3
    print("The sum of all of the integers from 1 to " + str(num)
          + " is " + str(sumOfInts(num)) + ". ")
    print("The sum of all of the squares of the integers from 1 to "
          + str(num) + " is " + str(sumOfSquares(num)) + ". ")
    num = 7
    print("The sum of all of the integers from 1 to " + str(num)
          + " is " + str(sumOfInts(num)) + ". ")
    print("The sum of all of the squares of the integers from 1 to "
          + str(num) + " is " + str(sumOfSquares(num)) + ". ")
    num = 10
    print("The sum of all of the integers from 1 to " + str(num)
          + " is " + str(sumOfInts(num)) + ". ")
    print("The sum of all of the squares of the integers from 1 to "
          + str(num) + " is " + str(sumOfSquares(num)) + ". ")
    print("Or we could thank a young Gauss for his derivation of the "
          + "sum of the first n numbers, given by (n(n+1))/2")
    print("There is a rather beautiful inductive proof over the "
          + "natural numbers showing that the sum of the squares of the "
          + "first n natural numbers is n(n+1)(2n+1)/6")

main()

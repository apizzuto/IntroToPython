'''
TITLE: Ex-4-3
AUTHOR: Alex Pizzuto
DATE: 2/8/17
DESCRIPTION: Computes averages of numbers in a list

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/8/17

'''

def average(numList):
    """Compute the average of a list of numbers"""
    summed=0
    i=0
    for num in numList:
        summed=summed+num
    ave=summed/len(numList)
    return ave


def main():
    numList = [4, 8, 3, 6]
    print("The average of the numbers in " + str(numList) + " is "
          + str(average(numList)) + ". ")
    numList = [1,2,3,4,5,6,7,8]
    print("The average of the numbers in " + str(numList) + " is "
          + str(average(numList)) + ". ")
    numList = [2]
    print("The average of the numbers in " + str(numList) + " is "
          + str(average(numList)) + ". ")
    numList = [10,20,30,43,25]
    print("The average of the numbers in " + str(numList) + " is "
          + str(average(numList)) + ". ")

main()

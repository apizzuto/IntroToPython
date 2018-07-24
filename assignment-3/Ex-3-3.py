'''
TITLE: Exercise 3-3
AUTHOR: Alex Pizzuto
DATE: February 1, 2017
DESCRIPTION: A program to print the number of strings of certain length from a character set of a given size 
MODIFICATION HISTORY AND OUTSIDE RESOURCES: last updated Feb. 01

'''
def numberOfStrings(numberOfCharacters, lengthOfString):
    num=numberOfCharacters**lengthOfString
    print('The number of strings of length {0} from a character set of size {1} is {2}.'.format(lengthOfString,numberOfCharacters,num))
for i in range(0,11):
    numberOfStrings(26,i)

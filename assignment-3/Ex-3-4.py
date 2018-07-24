'''
TITLE: Exercise 3-4
AUTHOR: Alex Pizzuto
DATE: February 1, 2017
DESCRIPTION: Program to switch contents of two variables.
MODIFICATION HISTORY AND OUTSIDE RESOURCES: last updated Feb. 01

Part (a) In order to make the switch, we need to introduce a third
receptacle temporarily. Say, for example, I have a cup. I would pour
the wine into the cup, then the coffee into the now empty goblet,
and then the wine into the now empty mug, and then to avoid the
chagrin of my roommates, I wash the cup.

'''
mugContents = input("What is in your mug? ")
gobletContents = input("What is in your goblet? ")
print("You started with " + mugContents + " in your mug and " + gobletContents
      + " in your goblet. ")
cupContents = gobletContents
gobletContents = mugContents
mugContents = cupContents
print("Presto, change-o!")
print("You now have " + mugContents + " in your mug and " + gobletContents
      + " in your goblet. ")

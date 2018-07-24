'''
TITLE: Ex-7-3
AUTHOR: Alex Pizzuto
DATE: 3/22/17
DESCRIPTION: Random Madlib

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/22/17

'''
from random import *
story="""
On one fine day, {name} awoke ready for the day,
as it was the first day of Comp150! {name}, eager
to make a good impression, had read through the entire
textbook {num} times before the first day. However,
as {name} looked at a clock, {name} realized that class
was starting in 5 minutes! In a rush, {name} jumped out
of bed before donning any {clothes}. Sprinting to class,
{name} was all in a tizzy and quite upset. Barging into
class, 10 minutes late, the whole class erupted in
laughter after noticing {name}'s lack of {clothes}.
In frustration, {name} left the class, thinking,
'well I guess reading the textbook {num} times
didn't help me make a good first impression.'
"""
nameList = ['Connor','Alex','Curtis','Jorge','Colleen','Marge','Hillary']
numList = ['5','68','92', '35', '21', '51', '1', '75']
clothesList = ['shirt','pants','glasses','underwear','jacket','tie']
myMadlibDictionary = dict()
myMadlibDictionary["name"] = nameList[randrange(len(nameList))]
myMadlibDictionary["num"] = numList[randrange(len(numList))]
myMadlibDictionary["clothes"] = clothesList[randrange(len(clothesList))]
print(story.format(**myMadlibDictionary))


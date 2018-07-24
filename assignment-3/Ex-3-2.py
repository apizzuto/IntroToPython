'''
TITLE: Exercise 3-2
AUTHOR: Alex Pizzuto
DATE: February 1, 2017
DESCRIPTION: A new madlib program
MODIFICATION HISTORY AND OUTSIDE RESOURCES: last updated Feb. 01

'''

name=input("Enter the name of a person: ")
num=input("Enter a number: ")
clothes=input("Enter an article of clothing: ")
story="""
On one fine day, {0} awoke ready for the day,
as it was the first day of Comp150! {0}, eager
to make a good impression, had read through the entire
textbook {1} times before the first day. However,
as {0} looked at a clock, {0} realized that class
was starting in 5 minutes! In a rush, {0} jumped out
of bed before donning any {2}. Sprinting to class,
{0} was all in a tizzy and quite upset. Barging into
class, 10 minutes late, the whole class erupted in
laughter after noticing {0}'s lack of {2}.
In frustration, {0} left the class, thinking,
'well I guess reading the textbook {1} times
didn't help me make a good first impression.'
"""
print(story.format(name, num, clothes))

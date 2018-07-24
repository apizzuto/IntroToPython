#!/usr/bin/env python3
"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
Adapted further by Alex Pizzuto
"""                                                  

storyFormat = """                                       
A long time ago, in a galaxy far, far away
there lived a Jedi named {name}. {name}
liked to move {thing} with the force, but {name}'s home 
planet, {planet}, had very
few {thing} around.  One day, a Jedi master
found {name} and discovered
they liked moving {thing}.  The Jedi master took 
{name} back to {different planet}, where {name} could
move as many {thing} as desired.  However,
{name} became homesick, so the
Jedi master brought {name} back to {planet},
leaving a large repository of {thing}.

Until next time...
"""                                                 

def tellStory():                                     
    userPicks = dict()                              
    addPick('name', userPicks)
    addPick('planet', userPicks)
    addPick('thing', userPicks)            
    addPick('different planet', userPicks)            
    story = storyFormat.format(**userPicks)
    print(story)
                                                    
def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter an example for a ' + cue + ': '
    response = input(prompt).strip() # 3.2 Windows bug fix
    dictionary[cue] = response                                                             

tellStory()                                         
input("Press Enter to end the program.")        

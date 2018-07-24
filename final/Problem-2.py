"""
TITLE: Final Exam Question 2
AUTHOR: Alex Pizzuto
DATE: 5/1/17
DESCRIPTION: Madlib Revisited

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 5/1/17

"""
def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys.
    Return a set containing all the keys from the format string.'''

    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1 # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key) # may add duplicates

    return set(keyList) # removes duplicates: no duplicates in a set

def addPick(cue, dictionary): # from madlibDict.py
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    promptFormat = "Enter a specific example for {name}: "
    prompt = promptFormat.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response                                                             


def getUserPicks(cues):
    '''Loop through the collection of cue keys and get user choices.
    Return the resulting dictionary.
    '''
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks   

def tellStory(storyFormat):
    '''storyFormat is a string with Python dictionary references embedded,
    in the form {cue}.  Prompt the user for the mad lib substitutions
    and then print the resulting story with the substitutions.
    '''
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story)

def main():
    handle = input("Enter a file name, or, type\n1 for 'Problem-2-storyFormat-1.txt' or\n2 for 'Problem-2-storyFormat-2.txt': ")
    if handle == "1":
        handle = "Problem-2-storyFormat-1.txt"
    elif handle =="2":
        handle = "Problem-2-storyFormat-2.txt"
    file = open(handle,'r')
    myStr = file.read()
    tellStory(myStr)
    file.close()
    input("Press Enter to end the program.")        


main()

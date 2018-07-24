'''
TITLE: Ex-5-4
AUTHOR: Alex Pizzuto
DATE: 2/22/17
DESCRIPTION: Computes all two-letter combinations of the
twenty-six letters and writes them to
'all-two-letter-strings.txt'
MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/22/17

'''
file = open("all-two-letter-strings.txt","w")
import string
alpha = list(string.ascii_uppercase)
for char1 in alpha:
    for char2 in alpha:
        combination = char1 + char2
        file.write(combination+"\n")
file.close()
    

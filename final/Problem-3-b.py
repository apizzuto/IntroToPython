"""
TITLE: Final Exam Question 3b
AUTHOR: Alex Pizzuto
DATE: 5/1/17
DESCRIPTION: All Three-Letter Strings

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 5/1/17

"""
file = open("Problem-3-b-output.txt","w")
import string
counter = 0
alpha = list(string.ascii_uppercase)
for char1 in alpha:
    for char2 in alpha:
        combination2 = char1 + char2
        for char3 in alpha:
            combination3 = char1 + char2 + char3
            file.write(combination3+"\n")
            counter+=1
print("We have generated {} strings.".format(counter))
file.close()

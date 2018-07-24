"""
TITLE: Final Exam Question 3a
AUTHOR: Alex Pizzuto
DATE: 5/1/17
DESCRIPTION: All Two-Letter Strings

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 5/1/17

"""
file = open("Problem-3-a-output.txt","w")
import string
counter = 0
alpha = list(string.ascii_uppercase)
for char1 in alpha:
    for char2 in alpha:
        combination = char1 + char2
        file.write(combination+" ")
        counter+=1
    file.write("\n\n")
print("We have generated {} strings.".format(counter))
file.close()
